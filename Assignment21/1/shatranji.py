import cv2
import numpy as np

img = np.zeros((800,800), dtype=np.uint8)
img[0:800, 0:800] = 0

for i in range(800):
    for j in range(800):
        a = (j // 100) % 2 
        b = (i // 100) % 2 
        if (a + b) % 2 == 0:
            img[i, j] = 255
            
img[0:799, 0] = 0
img[0:799, 799] = 0
img[0, 0:799] = 0
img[799, 0:799] = 0            
            
cv2.imwrite('1/shatranji.jpg', img)
cv2.imshow('picture', img)
cv2.waitKey()
