import cv2

lEye_detector = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
rEye_detector = cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")
smile_detector = cv2.CascadeClassifier("haarcascade_smile.xml")
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("photo/face.jpg", 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img2 = cv2.imread("photo/face.jpg", 0)
img2 = cv2.resize(img2, (0, 0), fx=0.5, fy=0.5)

eyeEmoji = cv2.imread("emoji/eye.png", 0)
smileEmoji = cv2.imread("emoji/smile.png", 0)

smiles = smile_detector.detectMultiScale(img, 2.1, minSize=(40, 40))
for (sx, sy, sw, sh) in smiles:
    # cv2.rectangle(img, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
    finalEmoji = cv2.resize(smileEmoji, (sw, sh))
    img[sy:sy+sh, sx:sx+sw] = finalEmoji
                
eyes = lEye_detector.detectMultiScale(img)
for (sx, sy, sw, sh) in eyes:
    # cv2.rectangle(img, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
    finalEmoji = cv2.resize(eyeEmoji, (sw, sh))
    img[sy:sy+sh, sx:sx+sw] = finalEmoji
    
for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] == 0:
                img[i, j] = img2[i, j]

cv2.imshow('output', img)
cv2.waitKey()