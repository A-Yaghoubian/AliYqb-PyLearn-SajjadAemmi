import cv2
import numpy as np

img = cv2.imread("input/flower_input.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = np.zeros(img.shape)

rows, cols = img.shape

# ret, thresh1 = cv2.threshold(src=result, thresh=100, maxval=255, type=cv2.THRESH_BINARY)
# result = thresh1 

for i in range(4, rows - 4):
    for j in range(4, cols - 4):
        small_img = img[i-4:i+5, j-4:j+5]
        small_img_1d = small_img.reshape(81)
        small_img_1d_sorted = np.sort(small_img_1d)
        result[i, j] = small_img_1d_sorted[40]

cv2.imwrite("output/flower_output.jpg", result)