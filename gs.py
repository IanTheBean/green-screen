# written by Ian Morgan for the STEAM night on May 19
# a simple green screen, although can be used with other colors
# feel free to read through and take for any use

# imports
import cv2
import numpy as np

class GreenScreen:
    def __init__(self):
        ## where all of the background images are stored
        self.background_images = ["beach.jpg", "chiefs.jpg", "cockpit.jpg", "graveyard.jpg", "minecraft.jpg", "news.jpg"]
        self.background_image_folder = "images/"
        self.background_image_count = len(self.background_images)
        self.current_image_count = 0
        self.background_image = cv2.imread(self.background_image_folder + self.background_images[self.current_image_count])
        

        ## start the video camera and grab an image
        self.camera_port = 0
        self.camera = cv2.VideoCapture(self.camera_port)
        callibrated_image = self.callibrate()

        ## find the average color of the image
        self.green_color = self.get_average_color(callibrated_image)
        self.green_buffer = 65
        
        ## set the upper and lower bounds of the green
        self.upper_green = np.array([
            (self.green_color[0] + self.green_buffer if self.green_color[0] + self.green_buffer < 255 else 255),
            (self.green_color[1] + self.green_buffer if self.green_color[1] + self.green_buffer < 255 else 255),
            (self.green_color[2] + self.green_buffer if self.green_color[2] + self.green_buffer < 255 else 255),
        ])
        self.lower_green = np.array([
            (self.green_color[0] - self.green_buffer if self.green_color[0] - self.green_buffer > 0 else 0),
            (self.green_color[1] - self.green_buffer if self.green_color[1] - self.green_buffer > 0 else 0),
            (self.green_color[2] - self.green_buffer if self.green_color[2] - self.green_buffer > 0 else 0),
        ])

        self.green_screen()
        

    # callibrate is called when the program first runs 
    # the camera is opened, then after a delay(for light exposure) a picture is taken
    def callibrate(self):
        exposure_frames = 30
        for i in range(exposure_frames):
            self.camera.read()
        ret, img = self.camera.read()
        return img
    
    # takes an image and averages out the color 
    def get_average_color(self, image_to_average):
        average_color_row = np.average(image_to_average, axis=0)
        average_color = np.average(average_color_row, axis=0)   
        return average_color

    def green_screen(self):
        while True:
            ret, frame = self.camera.read()
            frame = cv2.flip(cv2.resize(frame, (960, 540)), 1)
            background = cv2.resize(self.background_image, (960, 540))
            mask = cv2.inRange(frame, self.lower_green, self.upper_green)
            reserve = cv2.bitwise_and(frame, frame, mask = mask)
    
            final_image = frame - reserve
            final_image = np.where(final_image == 0, background, final_image)
        
    
            cv2.imshow("feed", final_image)

            k = cv2.waitKey(25)
            if k== 27:
                break
            elif k == 32:
                self.current_image_count += 1
                if self.current_image_count >= self.background_image_count:
                    self.current_image_count = 0
                self.background_image = cv2.imread(self.background_image_folder + self.background_images[self.current_image_count])
                
    
        self.camera.release()
        cv2.destroyAllWindows()


gs = GreenScreen()
