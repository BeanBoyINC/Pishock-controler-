from flask import Flask, request, send_from_directory
import webbrowser
from threading import Timer
from pishock import PiShock
import json
import os

app = Flask(__name__)

# Define the path to the JSON file
JSON_FILE = "credentials.json"

def load_credentials():
    """Load the credentials from the JSON file."""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    return None

# Load credentials from JSON file
credentials = load_credentials()

if credentials:
    USERNAME = credentials.get("username", "default_username")
    APIKEY = credentials.get("apikey", "default_apikey")
    CODE = credentials.get("code", "default_code")
else:
    USERNAME = "default_username"
    APIKEY = "default_apikey"
    CODE = "default_code"

pishock = PiShock(USERNAME, APIKEY, CODE)

@app.route('/')
def index():
    return send_from_directory('web', 'web_interface.html')

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    command = data.get('command')
    values = data.get('values', {})

    if command == 'shock':
        pishock.shock(intensity=int(values.get('shock_intensity', 50)),
                      duration=int(values.get('shock_duration', 5)))
    elif command == 'vibrate':
        pishock.vibrate(intensity=int(values.get('vibrate_intensity', 50)),
                        duration=int(values.get('vibrate_duration', 5)))
    elif command == 'beep':
        pishock.beep(duration=int(values.get('beep_duration', 5)))
    elif command == 'pulse':
        pishock.pulse(min_intensity=int(values.get('pulse_min_intensity', 10)),
                      max_intensity=int(values.get('pulse_max_intensity', 90)),
                      duration=int(values.get('pulse_duration', 5)),
                      interval=float(values.get('pulse_interval', 1.0)),
                      count=int(values.get('pulse_count', 5)))
    elif command == 'random':
        pishock.random_command(duration=int(values.get('random_duration', 5)))

    return {'status': 'success'}

def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

def start_web_server():
    Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    start_web_server()
