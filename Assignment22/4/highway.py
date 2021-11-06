import cv2
import numpy as np

HIGHWAY = []

for i in range(0, 15):
    HIGHWAY.append(cv2.imread(f"4/highway/h{i}.jpg", 0))
    
result = np.zeros((HIGHWAY[0].shape[0], HIGHWAY[0].shape[1]), dtype="uint8")

for i in range(0, 15):
    result += (HIGHWAY[i] // 15)

cv2.imwrite("4/result_highway.jpg", result)
# cv2.imshow('s', result)
cv2.waitKey()