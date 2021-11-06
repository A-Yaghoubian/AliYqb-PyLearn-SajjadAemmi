import cv2
import numpy as np

answer = np.zeros((250,1250), dtype=np.uint8)

akbar = cv2.imread("5/abdi.jpg", 0)
bahare = cv2.imread("5/rahnama.jpg", 0)
dim = (250, 250)

akbar = cv2.resize(akbar, dim)
bahare = cv2.resize(bahare, dim)

pic0 = akbar
pic4 = bahare
pic1 = akbar//2 + bahare//4
pic2 = akbar//2 + bahare//2
pic3 = akbar//4 + bahare//2

answer[0:250, 0:250] = pic0
answer[0:250, 250:500] = pic1
answer[0:250, 500:750] = pic2
answer[0:250, 750:1000] = pic3
answer[0:250, 1000:1250] = pic4

cv2.imwrite("5/result.jpg", answer)
cv2.imshow('a', answer)
cv2.waitKey()