#!/bin/bash

echo "📦 Setting up Pype..."
python3 -m venv .venv
source .venv/bin/activate

echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install praw requests rich tqdm

# Save requirements.txt for reproducibility
pip freeze > requirements.txt
echo "Dependencies installed and saved to requirements.txt"

echo "Configuring Reddit API..."
read -rp "Enter your Reddit username: " username
read -rsp "Enter your Reddit password: " password
echo
read -rp "Enter your Reddit client ID: " client_id
read -rp "Enter your Reddit client secret: " client_secret
read -rp "Enter your Reddit app name: " app_name

cat <<EOF > config.ini
[reddit]
username = $username
password = $password
client_id = $client_id
client_secret = $client_secret
app_name = $app_name
EOF

echo "Configuration saved to src/config.ini"
echo
echo "Setup complete Welcome!"
source .venv/bin/activate && python3 Pype.py

