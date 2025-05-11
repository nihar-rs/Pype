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
- `praw`, `requests`, `flask` (if using web integration)

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

  - create an app.
  - collect `client-id`, `client-secret`, `app_name`(The name of the app you created).

- use these credentials with the script.
