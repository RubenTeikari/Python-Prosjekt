Harvard CS50 Final Project - Automatic Fishing Bot for World of Warcraft
Project Overview
This project is a Python-based automated fishing bot for the game "World of Warcraft," leveraging the OpenCV library for image processing and automation.

Features
Screenshot Capture: The bot captures multiple screenshots per second of a specified window.
Color Detection: It searches for the correct color in BGR format, matching it against a predefined PNG file.
Mouse Movement: Upon detecting the correct color, the bot automatically moves the mouse pointer to the detected color's location.
Motion Detection: The bot then monitors the detected color area for any movement.
Automatic Click: When movement is detected, the bot performs a mouse click on the detected area followed by a keyboard action to cast the fishing line again.
Requirements
Python 3.x
OpenCV library (opencv-python package)
Installation
Clone the repository:

git clone https://github.com/Rubenteik/Harvard-cs50-final.git
cd Harvard-cs50-final
Install the required Python packages:

pip install -r requirements.txt
Usage
Ensure that "World of Warcraft" is running and the fishing interface is visible.
Run the bot script:
python fishing_bot.py
The bot will start taking screenshots, detecting the fishing bobber, and performing the necessary actions to fish automatically.
How It Works
Screenshot Capture: The bot captures screenshots at a high frequency to keep track of the fishing bobber.
Color Detection: It uses OpenCV to search for the predefined color in the BGR format, which corresponds to the fishing bobber.
Mouse Movement: Once the color is detected, the bot calculates the coordinates and moves the mouse pointer to that location.
Motion Detection: The bot monitors the area around the fishing bobber for any movement, indicating that a fish has been caught.
Automatic Click: Upon detecting movement, the bot clicks on the location to catch the fish and then recasts the fishing line.
Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
This project is part of the Harvard CS50 course.
Special thanks to the OpenCV community for their extensive documentation and support.
Feel free to modify this README further to suit your needs.
