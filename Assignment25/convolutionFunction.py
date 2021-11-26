import cv2
import numpy as np

def convolutionFunction(img, d, shape):
    rows, cols = shape
    result = np.zeros(img.shape)
    mask = np.ones((d, d)) / (d * d)

    for i in range((d // 2), rows - (d // 2)):
        for j in range((d // 2), cols - (d // 2)):
            small_img = img[i - (d // 2) : i + (d // 2) + 1, j - (d // 2) : j + (d // 2) + 1]
            result[i, j] = np.sum(small_img * mask)
            
    return result

img = cv2.imread("input/cow.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = convolutionFunction(img, 15, img.shape)
        
cv2.imwrite("output/conv15Func.jpg", result)