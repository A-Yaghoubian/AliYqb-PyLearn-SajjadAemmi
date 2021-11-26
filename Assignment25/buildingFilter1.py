import cv2
import numpy as np

img = cv2.imread("input/building.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = np.zeros(img.shape)
mask_33 = np.array([[-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]])

# mask_55 = np.ones((5, 5)) / 25

rows, cols = img.shape

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        small_img = img[i - 1 : i + 2, j - 1 : j + 2]
        result[i, j] = np.sum(small_img * mask_33)
        
cv2.imwrite('output/building1.png', result)