import cv2 as cv
import numpy as np
import pyautogui
import time



class FishingAgent:
    def __init__(self, main_agent) -> None:
        self.main_agent = main_agent
        self.fishing_target = cv.imread("C:\\Users\\bruta\Desktop\\Fishing Bot\\fishing\\assets\\fishing_target.png")
        self.fishing_thread = None

    def cast_lure(self):
        print("Casting...")
        pyautogui.press('1')
        time.sleep(2)
        self.find_lure()


    def find_lure(self):
        if self.main_agent.cur_img is not None:
            cur_img = self.main_agent.cur_img
            lure_location = cv.matchTemplate(
                cur_img,
                self.fishing_target,
                cv.TM_CCOEFF_NORMED)
            lure_loc_arr = np.array(lure_location)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(lure_loc_arr)
            print(max_loc)

            self.move_to_lure(max_loc)
       
       # cv.imshow("Match Template", lure_loc_arr)
       # cv.waitKey(0)

    def move_to_lure(self, max_loc):
        pyautogui.moveTo(max_loc[0], max_loc[1], 1, pyautogui.easeOutQuad)
        self.watch_lure(max_loc)

    def watch_lure(self, max_loc):
        watch_time = time.time()
        while True: 
            pixel = self.main_agent.cur_imgHSV[max_loc[1] + 25, max_loc[0]]
            print(pixel)
            
            if self.main_agent.zone == "Feralas" and self.main_agent.time == "night":
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