import pyautogui #Library that controls mouse movement and clicking behaviors
import time #Library that controls program sleeping

#TODO Need to add a way to track length of time from start of video
# to collecting reward in order to set the sleep timer properly

class atlas:

    def __init__(self):
        self.boost_available()

    try:
        def mouse_movement(self):
            pass

        def mouse_click(self, position):
            pass

        def mouse_scroll(self, direction):
            pass

        def boost_available(self): #Checks to see if boost timer is available
            print('Boost Availablke')
            self.play_boost_ad()

        def play_boost_ad(self):
            print('Playing Boost Ad')
            self.finish_ad()

        def navigate_to_shop(self):
            pass

        def play_free_ad(self):
            pass

        def finish_ad(self):
            print('Finished Ad')

        def collect_reward(self):
            pass

    except: restart_atlas(self)


    def restart_atlas(self):
        pass

auto = atlas()
