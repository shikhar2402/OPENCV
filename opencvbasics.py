import cv2
#command to read the image
image=cv2.imread('input.jpg')
#command to show the image
cv2.imshow('heelo',image)
cv2.waitKey(0)
print(image[0,0])#to show the rgb values at cordinate (0,0)



#command to split the image in their respective rgb colors
B,G,R=cv2.split(image)

print(B.shape)
cv2.imshow('red', R)
cv2.waitKey(0)
cv2.imshow('red', B)
cv2.waitKey(0)
cv2.imshow('red', G)

cv2.waitKey(0)

#you can actually increse the rgb values
merged=cv2.merge([B+100,G,R])
cv2.imshow('megered',merged)
cv2.waitKey(0)

#to create 3d pixel by deleteing the r/g/b colors by putting 0 array in their place
import numpy as np
zeros=np.zeros(image.shape[:2],dtype="uint8")
cv2.imshow("red",cv2.merge([zeros,zeros,R]))
cv2.imshow("green",cv2.merge([zeros,zeros,G]))
cv2.imshow("blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()

#DRAWING IMAGE USING CV2
#BLACK RECTANGLE
img=np.zeros((512,512,3),np.uint8)
img2=np.zeros((512,512),np.uint8)
cv2.imshow('black',img)
cv2.imshow('black rec',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#line
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.line(img,(100,100),(300,300),(255,123,3),1)
#first image then starting end point and then color and then thickness
cv2.imshow('black rec',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
#same is the case for drawing circlerectangle or any other figure you desires
#in case of circle you need to give a cordinate and the radius size ,colour, and thickness do it by yourself and reward yourself

#lets move on turn to add text in image
cv2.putText(img,'HELLO',(45,290),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0),3)
cv2.imshow("hello",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 


















