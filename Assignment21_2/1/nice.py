import cv2
import numpy as np

# Create nice1.jpg

img = np.zeros((255,255), dtype=np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i, j] = 255 - i
        
cv2.imwrite('1/nice1.jpg', img)
# cv2.imshow('nice', img)
cv2.waitKey()