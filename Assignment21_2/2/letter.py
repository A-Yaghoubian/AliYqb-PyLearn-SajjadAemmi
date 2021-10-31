import cv2
import numpy as np

img = np.zeros((600, 600), dtype=np.uint8)
img[:,:] = 255

def square(x, y):
    img[x-15:x+15, y-15:y+15] = 0

square(70, 300) 
#25
square(100, 275)
square(100, 325)
#20
square(130, 255)
square(130, 345)
#20
square(160, 235)
square(160, 365)
#20
square(190, 215)
square(190, 385)
#15
square(220, 200)
square(220, 400)
#15
square(250, 185)
square(250, 415)
#15
square(280, 170)
square(280, 430)
#10
square(310, 160)
square(310, 440)
#10
square(340, 150)
square(340, 450)
#10
square(370, 140)
square(370, 460)

#line
img[220:235, 215:385] = 0

cv2.imwrite('2/letterA.jpg', img)
cv2.imshow('s', img)
cv2.waitKey()