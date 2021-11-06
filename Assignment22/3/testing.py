import cv2

origin = cv2.imread("3/board - origin.bmp", 0)
test = cv2.imread("3/board - test.bmp", 0)
# flip test picture (mirror)
flipTest = cv2.flip(test, 1)
cv2.imwrite("3/flipTest.jpg", flipTest)

result = cv2.subtract(flipTest, origin)
cv2.imwrite("3/testing.jpg", result)

exager = result
for i in range(exager.shape[0]):
    for j in range(exager.shape[1]):
        if exager[i, j] != 0:
            exager[i, j] = 255
cv2.imwrite("3/exaggerated_result.jpg", exager)
# cv2.imshow('m', result)
cv2.waitKey()