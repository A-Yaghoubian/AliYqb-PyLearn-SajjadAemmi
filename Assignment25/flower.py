import cv2
import numpy as np

img = cv2.imread("input/flower_input.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = np.zeros(img.shape)

rows, cols = img.shape

for i in range(13, rows - 13):
    for j in range(13, cols - 13):
        if img[i, j] < 180:
            small_img = img[i-13:i+14, j-13:j+14]
            small_img_1d = small_img.reshape(729)
            small_img_1d_sorted = np.sort(small_img_1d)
            result[i, j] = small_img_1d_sorted[364]
        else:
            result[i, j] = img[i, j]

cv2.imwrite("output/flower_output.jpg", result)
