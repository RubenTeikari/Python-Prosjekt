import cv2 as cv
import numpy as np
import pyautogui
import time

class FishingAgent:
    def __init__(self, main_agent) -> None:
        self.main_agent = main_agent  # Reference to the main agent
        self.fishing_target = cv.imread("C:\\Users\\RubenDesktop\\Desktop\\Harvard-cs50-final\\fishing\\assets\\fishing_target.png")  # Load the fishing target image
        self.fishing_thread = None  # Initialize the fishing thread

    def cast_lure(self):
        print("Casting...")
        pyautogui.press('1')  # Simulate pressing the '1' key to cast the lure
        time.sleep(2)  # Wait for 2 seconds
        self.find_lure()  # Call the find_lure method

    def find_lure(self):
        if self.main_agent.cur_img is not None:  # Che1ck if the current image is not None
            cur_img = self.main_agent.cur_img  # Get the current image from the main agent
            lure_location = cv.matchTemplate(
                cur_img,
                self.fishing_target,
                cv.TM_CCOEFF_NORMED)  # Perform template matching to find the lure
            lure_loc_arr = np.array(lure_location)  # Convert the result to a numpy array

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(lure_loc_arr)  # Get the min and max values and their locations
            print(max_loc)  # Print the location of the maximum value

            self.move_to_lure(max_loc)  # Call the move_to_lure method with the max location

        # cv.imshow("Match Template", lure_loc_arr)  # Commented out display window
        # cv.waitKey(0)  # Commented out wait for a key press

    def move_to_lure(self, max_loc):
        pyautogui.moveTo(max_loc[0], max_loc[1], 1, pyautogui.easeOutQuad)  # Move the mouse to the lure location
        self.watch_lure(max_loc)  # Call the watch_lure method with the max location

    def watch_lure(self, max_loc):
        watch_time = time.time()  # Record the current time
        while True:
            pixel = self.main_agent.cur_imgHSV[max_loc[1] + 25, max_loc[0]]  # Get the pixel value at the lure location
            print(pixel)  # Print the pixel value

            if self.main_agent.zone == "Feralas" and self.main_agent.time == "night":  # Check if the zone is "Feralas" and the time is "night"
                if pixel[0] >= 25:
                    print("Bite detected!")
                    break

            if time.time() - watch_time >= 25:
                print("Fishing timeout")
                break

        self.pull_line()

    def pull_line(self):
        print("Pulling line!")
        pyautogui.click(button='right')
        time.sleep(0.010)

    def run(self):
        while True:
            self.cast_lure()
            time.sleep(5)