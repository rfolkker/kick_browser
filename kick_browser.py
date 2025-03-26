from flask import Flask, request, jsonify
import subprocess
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("KB_API_KEY")
ALLOWED_IP_PREFIX = os.getenv("KB_ALLOWED_IP_PREFIX", "192.168.68.")
VALIDATE_PORT = os.getenv("KB_PORT", "5000")
HOST = os.getenv("KB_HOST", "0.0.0.0")
PORT = 5000

# attempted to convert validate port to valid port
if isinstance(VALIDATE_PORT,int):
    PORT=VALIDATE_PORT
elif isinstance(VALIDATE_PORT,str):
    try:
        PORT = int(VALIDATE_PORT)
    except ValueError:
        PORT = 5000 # Set to a default value if invalid
# else PORT = 5000

# Initialize App
app = Flask(__name__)

# Versioned Kick function
@app.route("/api/v1/maintenance/kick", methods=["POST"])
def kick_browser():
    # Check for API key
    if request.headers.get("X-API-KEY") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 403
    
    # Validate internal IP address
    client_ip = request.remote_addr
    if not client_ip.startswith(ALLOWED_IP_PREFIX):
        return jsonify({"error": "Unauthorizedk"}), 403
    
    try:
        subprocess.run(["pkill", "-HUP", "chromium"], check=True)
        return jsonify({"message": "Chromium browser restarted"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
