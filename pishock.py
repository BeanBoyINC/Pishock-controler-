import requests
import json
import time
import random

class PiShock:
    def __init__(self, username, apikey, code, name="PiShock_Controller"):
        self.username = username
        self.apikey = apikey
        self.code = code
        self.name = name
        self.api_url = "https://do.pishock.com/api/apioperate/"
        self.headers = {'Content-Type': 'application/json'}

        # Initialize data for plotting
        self.time_data = []
        self.intensity_data = []

    def send_command(self, op, intensity, duration):
        data = {
            "Username": self.username,
            "Name": self.name,
            "Code": self.code,
            "Apikey": self.apikey,
            "Op": op,
            "Intensity": intensity,
            "Duration": duration
        }

        response = requests.post(self.api_url, headers=self.headers, data=json.dumps(data))

        if response.status_code == 200:
            print(f"Operation Succeeded: {response.text}")
        else:
            print(f"Error {response.status_code}: {response.text}")

    def shock(self, intensity, duration):
        self.send_command(0, intensity, duration)
        self.update_plot(intensity, duration)

    def vibrate(self, intensity, duration):
        self.send_command(1, intensity, duration)
        self.update_plot(intensity, duration)

    def beep(self, duration):
        self.send_command(2, intensity=0, duration=duration)
        self.update_plot(0, duration)

    def pulse(self, min_intensity, max_intensity, duration, interval, count):
        for _ in range(count):
            intensity = random.randint(min_intensity, max_intensity)
            self.shock(intensity, duration)
            time.sleep(interval)

    def update_plot(self, intensity, duration):
        current_time = time.time()
        self.time_data.append(current_time)
        self.intensity_data.append(intensity)

        # Update plot logic here
        # Note: Implement plot updating separately as needed

    def random_command(self, duration):
        intensity = random.randint(1, 100)  # Random intensity between 1 and 100
        self.shock(intensity, duration)
