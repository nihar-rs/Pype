#!/usr/bin/env python3

__description__ = "[Pype]: A reddit scraper that downloades your saved posts."
__author__ = "Nihar Satapathy"
__date__ = "4th May 2025"

import os
import re
import argparse
import configparser
from urllib.parse import urlparse

import praw
import requests
from rich import print
from tqdm import tqdm

def edit_filename(title, max_length=100):
    title = re.sub(r'[<>:"/\\|?*]', "", title)
    title = re.sub(r"\s+", "_", title)
    return title[:max_length].strip("_")


def login_reddit():
    config = configparser.ConfigParser()
    config.read("config.ini")

    try:
        reddit = praw.Reddit(
            username = config["reddit"].get("username", ""),
            password = config["reddit"].get("password", ""),
            client_id = config["reddit"].get("client_id", ""),
            client_secret = config["reddit"].get("client_secret", ""),
            app_name = config["reddit"].get("app_name", ""),
            user_agent = f"{config["reddit"].get("app_name", "")} by /u/{config["reddit"].get("username", "")}"
        )
        user = reddit.user.me()
        if not user:
            raise Exception("Login failed. Check credentials.")
        print(f"✅ Logged in as: {user}")
        return reddit
    except Exception as e:
        print(f"❌ {e}")
        exit(1)


def download_from_items(items, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    downloaded = []

    for item in tqdm(items, desc="Downloading", unit="file"):
        if isinstance(item, praw.models.Submission):
            url = item.url
            parsed = urlparse(url)
            ext = os.path.splitext(parsed.path)[-1].lower()

            if ext in [".jpg", ".jpeg", ".png", ".gif", ".mp4"]:
                title_safe = edit_filename(item.title)
                filename = f"{title_safe}{ext}"
                filepath = os.path.join(save_dir, filename)

                try:
                    response = requests.get(url, stream=True, timeout=10)
                    response.raise_for_status()
                    with open(filepath, "wb") as f:
                        for chunk in response.iter_content(8192):
                            f.write(chunk)
                    downloaded.append(filename)
                except Exception as e:
                    print(f"⚠️ Failed to download {url} — {e}")
    print(f"✅ Finished. {len(downloaded)} files downloaded to '{save_dir}'.")


def main():
    parser = argparse.ArgumentParser(description="Pype_v0.2 — Reddit Media Downloader")
    parser.add_argument("--subreddit", help="Subreddit name to download media from")
    parser.add_argument("--saved", action="store_true", help="Download saved media from your account")
    parser.add_argument("--limit", type=int, default=10, help="Number of posts to download")
    parser.add_argument("--nsfw", action="store_true", help="Include NSFW posts")
    parser.add_argument("--output", default="Downloads", help="Output directory for downloads")
    args = parser.parse_args()

    reddit = login_reddit()

    if args.subreddit:
        subreddit = reddit.subreddit(args.subreddit)
        posts = subreddit.hot(limit=args.limit)
        if not args.nsfw:
            posts = [p for p in posts if not p.over_18]
        download_from_items(posts, args.output)

    elif args.saved:
        user = reddit.user.me()
        posts = user.saved(limit=args.limit)
        if not args.nsfw:
            posts = [p for p in posts if not p.over_18]
        download_from_items(posts, args.output)

    else:
        print("Insufficient Arguments! [Please specify either --subreddit <name> or --saved]")
        print("Use command [Pype -h for help.]")


if __name__ == "__main__":
    main()

