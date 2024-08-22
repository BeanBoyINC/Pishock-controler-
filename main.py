import sys
import json
import os
import tkinter as tk
from tkinter import simpledialog
from pishock import PiShock
from gui import create_gui
import web_server  

JSON_FILE = "credentials.json"

def save_credentials(username, apikey, code):
    """Save the provided credentials to the JSON file."""
    with open(JSON_FILE, "w") as f:
        json.dump({"username": username, "apikey": apikey, "code": code}, f)

def load_credentials():
    """Load the credentials from the JSON file."""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    return None

def prompt_for_credentials():
    """Prompt the user for credentials using a Tkinter GUI."""
    root = tk.Tk()
    root.withdraw()  

    username = simpledialog.askstring("Input", "Enter your username:")
    apikey = simpledialog.askstring("Input", "Enter your API key:")
    code = simpledialog.askstring("Input", "Enter your code:")

    if username and apikey and code:
        save_credentials(username, apikey, code)
        return {"username": username, "apikey": apikey, "code": code}
    else:
        raise ValueError("All fields are required.")

def main():
    credentials = load_credentials()

    if credentials:
        username = credentials["username"]
        apikey = credentials["apikey"]
        code = credentials["code"]
    else:
        credentials = prompt_for_credentials()
        username = credentials["username"]
        apikey = credentials["apikey"]
        code = credentials["code"]

    pishock = PiShock(username, apikey, code)

    if '--web' in sys.argv:
        print("Starting web server...")
        web_server.start_web_server()
    else:
        print("Starting GUI...")
        create_gui(pishock)

if __name__ == "__main__":
    main()
