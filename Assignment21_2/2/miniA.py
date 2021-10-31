import cv2
import numpy as np

img = np.zeros((300, 200), dtype=np.uint8)
img[:,:] = 255

img[75:100, 70:130] = 0
img[100:180, 70:90] = 0
img[100:180, 110:130] = 0
img[128:142, 80:120] = 0

cv2.imwrite('2/miniA.jpg', img)
cv2.imshow('s', img)
cv2.waitKey()