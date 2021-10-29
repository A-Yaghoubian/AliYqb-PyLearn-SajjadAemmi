import cv2

img = cv2.imread('Assignment 21/3.jpg', 0)
new_img = cv2.imread('Assignment 21/3.jpg', 0)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        new_img[img.shape[0] - 1 - i, img.shape[1] - 1 - j] = img[i, j]
        
cv2.imwrite('3/happy.jpg', new_img)
# cv2.imshow('p', new_img)
cv2.waitKey()