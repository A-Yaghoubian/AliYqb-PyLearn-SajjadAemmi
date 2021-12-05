import cv2
import numpy as np

img = cv2.imread("input/lowConFemale.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equ = cv2.equalizeHist(img)

alpha = 1.5 
beta = 0 
adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

alpha = 2 
beta = -150 
adjusted2 = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

alpha2 = 1.5
beta2 = 0
new_image = cv2.addWeighted(img, alpha2, np.zeros(img.shape, img.dtype), 0, beta2)

cv2.imshow('original', img)
cv2.imshow('equ', equ)
cv2.imshow('adjusted', adjusted)
cv2.imshow('adjusted2', adjusted2)
cv2.imshow('new', new_image)
cv2.waitKey()