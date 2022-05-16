import cv2
images = ["beach.jpg", "chiefs.jpg", "cockpit.jpg", "graveyard.jpg", "minecraft.jpg", "news.jpg"]
img = cv2.imread("./images/" + images[0]) # load a dummy image
img = cv2.resize(img, (960, 540))
while(1):
    cv2.imshow('img', img)
    k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    else:
        img = cv2.imread("./images/" + images[k-49])
        img = cv2.resize(img, (960, 540))
        print (k) # else print its value