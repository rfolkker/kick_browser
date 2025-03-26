# kick_browser
Restart kiosk browser as a web endpoint with simple API key and IP validation

## How to use
* put the files from this git repo into your opt folder with the folder name kick_browser
* switch into your git repo folder
* Create your python environment
* Install the Flask and dotenv dependencies into your python virtual environment (via requirements file)
* Create your environment file
* Copy the kick_browser.service file into your etc/systemd/system folder
* drop back one folder
* Copy the kick_browser into the opt folder
* Restart Systemd and start the new service
* Trigger the enpoint to see if it works

``` bash
git clone <this repository>
cd ./kick_browser
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
cat > .env << EOF
KB_API_KEY="YOUR_API_KEY"
KB_ALLOWED_IP_PREFIX="10.0.0."
KB_HOST="0.0.0.0"
EOF
sudo cp ./kick_browser.service /etc/systemd/system
cd ..
sudo cp -p ./kick_browser /opt/kick_browser/
sudo systemctl daemon-reload
sudo systemctl enable kick_browser
sudo systemctl start kick_browser
```

Please note: You will want to change YOUR_API_KEY to something custom for you (or if you can generate API keys, use a service to generate and track it)
Also, the KB_ALLOWED_IP_PREFIX should be set to the subnet or computer you want to limit access to.

### It should go without saying, this does trigger a system event on a computer, do not expose this to the internet.
