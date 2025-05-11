# Pype

A simple Python script to download images, GIFs, and videos from your **saved posts** on Reddit using the Reddit API.

## 🚀 Features

- Downloads media from saved Reddit posts
- Supports `.jpg`, `.png`, `.gif`, `.mp4`, `.jpeg`
- Automatically names files based on post titles
- Uses your Reddit credentials securely from a config file
- Simple command-line interface.

## 🔧 Requirements

- Python 3.7+
- Reddit API credentials
- `praw`, `requests`

## Installation:

- Give execution permission

```bash
chmod +x setup.sh
```

- Run setup

```bash
./setup.sh
```

- Run the script:

```python3
python3 src/Pype.py
```

## API:

- [Reddit API](https://www.reddit.com/prefs/apps)

    - Go to the link above and click: `create an app`
    - name: `any name(example: test)`
    - type: `script`
    - redirect url: `"http://localhost:8080"`
    - After you create an app, you should find your client-id under: `personal use script`
    - secret should be listed following: `secret`
    - collect: `client-id`, `client-secret`, `app_name`(The name of the app you created).

- use these credentials with the script.
