import cv2

a = cv2.imread("1/a.tif", 0)
b = cv2.imread("1/b.tif", 0)

result = cv2.subtract(b, a)
for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        if result[i, j] == 0:
            result[i, j] = 255
        elif result[i, j] == 255:
            result[i, j] = 0
      
cv2.imwrite("1/Decryption.jpg", result)
cv2.imshow("result", result)
cv2.waitKey()