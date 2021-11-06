import cv2
import random

img = cv2.imread("7/images.jpg", 0)
x, y = img.shape

for i in range(random.randint(300, 500)):
    color = random.randint(50, 150)
    noiseX = random.randint(0, x-1)
    noiseY = random.randint(0, y-1)
    img[noiseX, noiseY] = color
    
cv2.imwrite("7/noiseImage.jpg", img)
cv2.imshow('output', img)
cv2.waitKey()