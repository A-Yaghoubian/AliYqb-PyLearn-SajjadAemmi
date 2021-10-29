import cv2

wolf_img = cv2.imread('Assignment 21/4.jpg', 0)

for i in range(wolf_img.shape[0]):
    for j in range(wolf_img.shape[1]):
        if wolf_img[i, j] < 130:
            wolf_img[i, j] = 0
            
cv2.imwrite('4/wolf.jpg', wolf_img)
# cv2.imshow('pic', wolf_img)
cv2.waitKey()