# written by Ian Morgan for the STEAM night on May 17
# a simple green screen, although can be used with other colors
# feel free to read through and take for any use

# imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

class GreenScreen:
    def __init__(self):
        ## where all of the background images are stored
        self.background_images = ["beach.jpg", "chiefs.jpg", "cockpit.jpg", "graveyard.jpg", "minecraft.jpg", "news.jpg"]
        self.background_image_folder = "/images/"
        self.background_image_count = len(self.background_images)

        ##
        self.camera_port = 0
        self.camera = cv2.VideoCapture(self.camera_port)
        callibrated_image = self.callibrate()
        cv2.imshow("image", callibrated_image)
        cv2.waitKey(0)
            



    # callibrate is called when the program first runs 
    # the camera is opened, then after a delay(for light exposure) a picture is taken
    def callibrate(self):
        exposure_frames = 30
        for i in range(exposure_frames):
            self.camera.read()
        ret, img = self.camera.read()
        return img
    
    # takes an image and averages out the color 
    def get_average_color():
        pass
gs = GreenScreen()
