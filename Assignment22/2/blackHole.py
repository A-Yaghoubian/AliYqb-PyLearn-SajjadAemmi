import cv2
import numpy as np

hole = []
for i in range(1, 5):
    for j in range(1, 6):
        img = cv2.imread(f"2/black hole/{i}/{j}.jpg", 0)
        hole.append(img)
        row, col = img.shape
    
result1 = np.zeros((row, col), dtype="uint8")
for image in range(0, 5):
    result1 += hole[image] // 6

result2 = np.zeros((row, col), dtype="uint8")
for image in range(5, 10):
    result2 += hole[image] // 6
    
result3 = np.zeros((row, col), dtype="uint8")
for image in range(10, 15):
    result3 += hole[image] // 6
    
result4 = np.zeros((row, col), dtype="uint8")
for image in range(15, 20):
    result4 += hole[image] // 6

final = np.zeros((2*row, 2*col), dtype="uint8")
final[0:row, 0:col] = result1
final[0:row, col:2*col] = result2
final[row:2*row, 0:col] = result3
final[row:2*row, col:2*col] = result4

cv2.imwrite("2/final.jpg", final)
# cv2.imshow('s', final)
cv2.waitKey()