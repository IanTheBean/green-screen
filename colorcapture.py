import cv2
from cv2 import waitKey
import numpy as np

# callibrate is called when the program first runs 
# the camera is opened, then after a delay(for light exposure) a picture is taken
# the average of every pixel in the image is taken and returned
def callibrate():
    video = cv2.VideoCapture(0)
    cont = 0
    while cont <= 5:
        ret, frame = video.read()
        if cont >= 5:
            
            frame = cv2.resize(frame, (640, 480))
            average_color_row = np.average(frame, axis=0)
            average_color = np.average(average_color_row, axis=0)
            d_img = np.ones((312,312,3), dtype=np.uint8)
            d_img[:,:] = average_color
            cv2.imshow('Source image',frame)
            cv2.imshow('Average Color',d_img)
            waitKey(0)
            print(average_color)
        cont += 1
