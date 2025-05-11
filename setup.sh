#!/bin/bash

#Install dependancies:

echo "Installing dependencies: "
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
echo -e "\nSetup complete!"


echo "Setup reddit config: "
echo -n "Enter your Reddit username: "
read -r username

echo -n "Enter your Reddit password: "
read -rs password
echo

echo -n "Enter your Reddit client ID: "
read -r client_id

echo -n "Enter your Reddit client secret: "
read -r client_secret

echo -n "Enter your Reddit app name:"
read -r app_name

cat <<EOF > src/config.ini
[reddit]
username = $username
password = $password
client_id = $client_id
client_secret = $client_secret
app_name = $app_name
EOF
echo "✅ Configuration saved to config.ini"

python3 src/Pype.py
