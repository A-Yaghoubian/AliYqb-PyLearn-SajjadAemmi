import cv2

female = cv2.imread('Assignment 21/1.jpg', 0)
male = cv2.imread('Assignment 21/2.jpg', 0)

for i in range(female.shape[0]):
    for j in range(female.shape[1]):
        female[i, j] = 255 - female[i, j]

for i in range(male.shape[0]):
    for j in range(male.shape[1]):
        male[i, j] = 255 - male[i, j]

cv2.imwrite('2/male.jpg', male)
cv2.imwrite('2/female.jpg', female)

# cv2.imshow('m', male)
# cv2.imshow('f', female)
cv2.waitKey()