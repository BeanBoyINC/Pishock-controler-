# PiShock Controller

This project provides a Python-based controller for the PiShock device, allowing you to send various commands to the device via a web interface or a graphical user interface (GUI). The project consists of a Python backend that interacts with the PiShock API and a web-based frontend to control the device.

## Features

- **Shock**: Control the intensity and duration of the shock.
- **Vibrate**: Adjust the intensity and duration of vibration.
- **Beep**: Control the duration of the beep.
- **Pulse**: Set the parameters for pulsing commands including intensity, duration, interval, and count.
- **Random**: Send random shock commands.

## Project Structure

- **`main.py`**: The main entry point for running either the GUI or web server.
- **`pishock.py`**: Contains the `PiShock` class which handles communication with the PiShock API.
- **`web_server.py`**: Sets up a Flask web server to serve the web interface and handle commands.
- **`web/web_interface.html`**: The HTML frontend for interacting with the PiShock device through a web browser.

## Setup
run **`pip install -r requirements.txt `**: to install all the stuff you need to get it up and running.

## Running the program

You can do **`python main.py`**: to run normaly with a little gui.
you can also do **`python main.py --web`**: to open a little web interface if you like that more.

## What it looks like

![Main_GUI](https://imgur.com/a/I2REgFS)
