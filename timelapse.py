from goprocam import GoProCamera
from goprocam import constants
import argparse
import keyboard
import os

"""
TimeLapse class that handles managing the timelapse capture from GoPro
"""
class Timelapse:

    def __init__(self, save_name, capture_int):
        # Might need GoPro IP Address and MAC Address to initialize
        self.gopro = GoProCamera.GoPro(camera='HERO4 Black', webcam_device="usb9")
        self.interval = capture_int
        self.COUNT = 0
        self.save_name = save_name
        # Create folder to save locally
        self.save_path = os.path.join(os.getcwd(), save_name)
        os.makedirs(self.save_path)

        # thread pool of Google Drive savers
        
    def run(self):
        running = True
        while running:
            photo = self.gopro.take_photo(self.interval)
            self.gopro.downloadLastMedia(photo, os.path.join(self.save_path, self.save_name + "_" + str(self.COUNT) + ".jpg"))
            self.gopro.delete("last")
            
            # Spawn thread to save to Google Drive

            self.COUNT += 1
            if keyboard.is_pressed('q'):
                print("Shutting Timelapse Down")
                running = False

        self.shutdown()

    def shutdown(self):
        print("Shutting Down Timelapse...")
        # join last remaining threads

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str, help="The name of the folder to save timelapse to on Google Drive")
    parser.add_argument('capture_int', type=int, help="The interval [in seconds] between photo captures")
    args = parser.parse_args()
    
    tl = Timelapse(args.name, args.capture_int)
    tl.run()