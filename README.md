# Pype

A simple Python script to download images, GIFs, and videos from Reddit using the Reddit API.

## 🚀 Features

- Downloads media from saved Reddit posts
- Downloads media from specified-subreddits 
- Supports `.jpg`, `.png`, `.gif`, `.mp4`, `.jpeg`
- Automatically names files based on post titles
- Uses your Reddit credentials securely from a `.ini` file

### v0.2.0 Updates:

- Resume support → skips files already downloaded
- Parallel downloads with ThreadPoolExecutor
- NSFW toggle (--nsfw)
- NSFW content goes into <output>/NSFW/<subreddit>/...
- Cleaner graphics using tqdm
- Slightly safer filename handling

## 🔧 Requirements

- Python 3.7+
- Reddit API credentials
- `praw`, `requests`, `rich`, `tqdm`

## Installation:

- Goto: 📁 src/
```bash
cd src/
```

- Give execution permission
```bash
chmod +x setup.sh
```

- Run setup
```bash
./setup.sh
```
- This command should display the help message.

- Or run the script manually:
```bash
python3 Pype.py -h
```

## API:
[!NOTE] Get the reddit api credentials before you run the script as you will need them to run it.

- [Reddit API](https://www.reddit.com/prefs/apps)

    - Go to the link above and click: `create an app`
    - name: `any name(example: test)`
    - type: `script`
    - redirect url: `"http://localhost:8080"`
    - After you create an app, you should find your client-id under: `personal use script`
    - secret should be listed following: `secret`
    - collect: `client-id`, `client-secret`, `app_name`(The name of the app you created).

- use these credentials with the script.
