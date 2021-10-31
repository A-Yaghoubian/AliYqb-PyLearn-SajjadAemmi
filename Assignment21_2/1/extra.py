import cv2
import numpy as np

# Create nice2.jpg

img = np.zeros((510,510), dtype=np.uint8)

for i in range(0, 510, 2):
    for j in range(510):
        img[i, j] = (510 - i) // 2
        
cv2.imwrite('1/nice2.jpg', img)
cv2.imshow('nice', img)
cv2.waitKey()