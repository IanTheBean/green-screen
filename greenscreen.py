import cv2
import numpy as np

def start_screen():
    video = cv2.VideoCapture(0) # start the webcam
    image = cv2.imread("weather.jpg") # get the background image
    color_buffer = 67 #
    green_color = callibrate()
    u_green = np.array([
        (green_color[0] + color_buffer if green_color[0] + color_buffer < 255 else 255),
        (green_color[1] + color_buffer if green_color[1] + color_buffer < 255 else 255),
        (green_color[2] + color_buffer if green_color[2] + color_buffer < 255 else 255),
    ])
    l_green = np.array([
        (green_color[0] - color_buffer if green_color[0] - color_buffer > 0 else 0),
        (green_color[1] - color_buffer if green_color[1] - color_buffer > 0 else 0),
        (green_color[2] - color_buffer if green_color[2] - color_buffer > 0 else 0),
    ])
    while True:
    
        ret, frame = video.read()
    
        frame = cv2.flip(cv2.resize(frame, (960, 540)), 1)
        image = cv2.resize(image, (960, 540))
    
        
        
    
        mask = cv2.inRange(frame, l_green, u_green)
        res = cv2.bitwise_and(frame, frame, mask = mask)
    
        f = frame - res
        f = np.where(f == 0, image, f)
        
    
        cv2.imshow("mask", f)
    
        if cv2.waitKey(25) == 27:
            break
    
    video.release()
    cv2.destroyAllWindows()

def callibrate():
    video = cv2.VideoCapture(0)
    cont = 0
    while cont <= 5:
        ret, frame = video.read()
        if cont >= 5:
            frame = cv2.resize(frame, (640, 480))
            average_color_row = np.average(frame, axis=0)
            average_color = np.average(average_color_row, axis=0)
            return average_color
        cont += 1

start_screen()