#!/usr/bin/env python3

import os
import re
import configparser
from urllib.parse import urlparse

import praw
import requests


config = configparser.ConfigParser()
config.read("src/config.ini")

username = config["reddit"].get("username", "")
password = config["reddit"].get("password", "")
client_id = config["reddit"].get("client_id", "")
client_secret = config["reddit"].get("client_secret", "")
app_name = config["reddit"].get("app_name", "")


def edit_filename(title, max_length=100):
    title = re.sub(r'[<>:"/\\|?*]', "", title)
    title = re.sub(r"\s+", "_", title)
    return title[:max_length].strip("_")


def main():
    try:
        reddit = praw.Reddit(
            username=username,
            password=password,
            client_id=client_id,
            client_secret=client_secret,
            user_agent=f"{app_name} by /u/{username}",
        )
        user = reddit.user.me()
        if user is None:
            print("❌ Login failed. Check your credentials.")
            return

        print(f"✅ Logged in as: {user}")

    except Exception as e:
        print(f"❌ Login failed: {str(e)}")
        return

    save_dir = "Downloads"
    os.makedirs(save_dir, exist_ok=True)
    downloaded = []
    limit = 50

    for item in user.saved(limit=limit):
        if isinstance(item, praw.models.Submission):
            url = item.url
            parsed = urlparse(url)
            ext = os.path.splitext(parsed.path)[-1].lower()

            if ext in [".jpg", ".png", ".gif", ".mp4", ".jpeg"]:
                title_safe = edit_filename(item.title)
                filename = f"{title_safe}{ext}"
                filepath = os.path.join(save_dir, filename)

                try:
                    print(f"⬇️ Downloading: {filename} from {url}")
                    response = requests.get(url, stream=True, timeout=10)
                    response.raise_for_status()

                    with open(filepath, "wb") as f:
                        for chunk in response.iter_content(8192):
                            f.write(chunk)

                    downloaded.append(filename)
                except Exception as e:
                    print(f"⚠️ Failed to download {url} — {e}")
            else:
                print(f"⏩ Skipped unsupported file: {url}")

    print(f"\n✅ Finished. {len(downloaded)} files downloaded to '{save_dir}'.")


if __name__ == "__main__":
    main()
