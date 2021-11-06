import cv2

myPicture = cv2.imread("6/me.jpg", 0)

inverted = 255 - myPicture
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blurred = 255 - blurred

sketch = myPicture // inverted_blurred
sketch = 255 * sketch

cv2.imwrite("6/Art.jpg", sketch)
cv2.imshow("me", sketch)
cv2.waitKey()