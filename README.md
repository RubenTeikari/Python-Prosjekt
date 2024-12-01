# Harvard CS50 Final Project - Automatic Fishing Bot for World of Warcraft

## Project Overview
This project is a Python-based automated fishing bot for the game "World of Warcraft," leveraging the OpenCV library for image processing and automation.

## Features
- **Screenshot Capture**: The bot captures multiple screenshots per second of a specified window.
- **Color Detection**: It searches for the correct color in BGR format, matching it against a predefined PNG file.
- **Mouse Movement**: Upon detecting the correct color, the bot automatically moves the mouse pointer to the detected color's location.
- **Motion Detection**: The bot then monitors the detected color area for any movement.
- **Automatic Click**: When movement is detected, the bot performs a mouse click on the detected area followed by a keyboard action to cast the fishing line again.

## Requirements
- Python 3.x
- OpenCV library (`opencv-python` package)
- Pillow library (`pillow` package)
- PyAutoGUI library (`pyautogui` package)
- NumPy library (`numpy` package)

## Installation
1. **Clone the repository**: git clone https://github.com/Rubenteik/Harvard-cs50-final.git
   cd Harvard-cs50-final
2. **Install the required Python packages**
3. **Run the script**: python main.py

## Acknowledgements
This project was developed as part of the Harvard CS50 course.
Developed by Ruben Teikari.