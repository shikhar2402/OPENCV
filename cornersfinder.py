#Shi-Tomasi Corner Detector
#cv2.goodFeaturesToTrack()

import cv2
#command to read the image
image=cv2.imread('chess.jpg')
#ocnvert into grayscale
images=cv2.imread('chess.jpg',0)
#command to show the image
cv2.imshow('heelo',image)
cv2.waitKey(0)
print(image[0,0])

corners=cv2.goodFeaturesToTrack(images,100,0.01,15)
#100 is used for max. number of corner to be found
#0.01 is the quality factor that defimes the minimal quality of image
#15 is used for distance between nearest corners

for corner in corners:
    x,y=corner[0]
    print(x)
    x=int(x)
    y=int(y)
    cv2.rectangle(image,(x-10,y-10),(x+10,y+10),(0,255,0),-1)
cv2.imshow('corners are',image)
cv2.waitKey()
cv2.destroyAllWindows()
    