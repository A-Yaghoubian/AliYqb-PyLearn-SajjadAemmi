import random
import cv2

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("photo/team2.jpg", 0)
replaceImg = cv2.imread("photo/team2.jpg", 0)

emoji1 = cv2.imread("emoji/up.png", 0)
emoji2 = cv2.imread("emoji/drunk.png", 0)
emoji3 = cv2.imread("emoji/glass.png", 0)
emojiList = [emoji1, emoji2, emoji3]

faces = face_detector.detectMultiScale(img, 1.3)

for i, face in enumerate(faces):
    x, y, w, h = face
    finalEmojy = cv2.resize(random.choice(emojiList), (w, h))
    img[y:y+h, x:x+w] = finalEmojy

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i, j] == 0:
            img[i, j] = replaceImg[i, j]

cv2.imshow('result.jpg', img)
cv2.waitKey()