import random
import cv2
import cvzone

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
lEye_detector = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
rEye_detector = cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")
smile_detector = cv2.CascadeClassifier("haarcascade_smile.xml")

video_cap = cv2.VideoCapture(0)
current_state = 0

emoji1 = cv2.imread("emoji/up.png", cv2.IMREAD_UNCHANGED)
emoji2 = cv2.imread("emoji/drunk.png", cv2.IMREAD_UNCHANGED)
emoji3 = cv2.imread("emoji/glass.png", cv2.IMREAD_UNCHANGED)
emojiList = [emoji1, emoji2, emoji3]
eyeEmoji = cv2.imread("emoji/eye.png", cv2.IMREAD_UNCHANGED)
smileEmoji = cv2.imread("emoji/smile.png", cv2.IMREAD_UNCHANGED)

while True:    
    ret, frame = video_cap.read()
    if ret == False:
        break
    
    cv2.putText(frame, "(1) = Emoji Face", (10, 30), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (74, 26, 106), 1)
    cv2.putText(frame, "(2) = Fuuny Face", (10, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (148, 114, 68), 1)
    cv2.putText(frame, "(3) = Pixelate Face", (10, 110), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (74, 26, 106), 1)
    cv2.putText(frame, "(4) = Blur Face", (10, 150), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (148, 114, 68), 1)
    cv2.putText(frame, "(5) = Reverse Face", (10, 190), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (74, 26, 106), 1)
    cv2.putText(frame, "(0) = Raw Face", (10, 230), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (0, 255, 204), 1)
    cv2.putText(frame, "(Esc) = Quit", (10, 270), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (0, 255, 204), 1)
    
    # frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    k = cv2.waitKey(1)
    if k == 49 or current_state == 49: # k == ord("1")
        current_state = 49
        
        FACES = face_detector.detectMultiScale(frame, 1.3)
        for (x, y, w, h) in FACES:
            finalEmojy = cv2.resize(random.choice(emojiList), (w, h))
            frame = cvzone.overlayPNG(frame, finalEmojy, [x, y])
        
        k = cv2.waitKey(2)
        if k == 48: # k == ord("0")
            current_state = 0
        
    elif k == 50 or current_state == 50: # k == ord("2")
        current_state = 50
        
        # REYE = rEye_detector.detectMultiScale(frame_gray)
        LEYE = lEye_detector.detectMultiScale(frame, 1.1, maxSize=(100, 100))  # minNeighbors=45
        for (x, y, w, h) in LEYE:
            finalEmojy = cv2.resize(eyeEmoji, (w, h))
            frame = cvzone.overlayPNG(frame, eyeEmoji, [x, y])
            
        SMILE = smile_detector.detectMultiScale(frame, 1.34, 29) # 1.8,minNeighbors=22
        for (x, y, w, h) in SMILE:
            finalEmojy = cv2.resize(smileEmoji, (w, h))
            frame = cvzone.overlayPNG(frame, finalEmojy, [x, y])
            
        k = cv2.waitKey(2)
        if k == 48: # k == ord("0")
            current_state = 0
    
    elif k == 51 or current_state == 51: # k == ord("3")
        current_state = 51
        
        FACES = face_detector.detectMultiScale(frame, 1.3)
        for (x, y, w, h) in FACES:            
            blurred = frame[y:y+h, x:x+w]
            pixlated = cv2.resize(blurred, (15, 15), interpolation=cv2.INTER_LINEAR)
            output = cv2.resize(pixlated, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = output
        
        k = cv2.waitKey(2)
        if k == 48: # k == ord("0")
            current_state = 0
    
    elif k == 52 or current_state == 52: # k == ord("4")
        current_state = 52
        
        FACES = face_detector.detectMultiScale(frame, 1.3)
        for (x, y, w, h) in FACES:
            blurred = cv2.GaussianBlur(frame[y:y+h, x:x+w], (25, 25), 35)
            frame[y:y+h, x:x+w] = blurred
        
        k = cv2.waitKey(2)
        if k == 48: # k == ord("0")
            current_state = 0
        
    elif k == 53 or current_state == 53: # k == ord("5")
        current_state = 53
        
        FACES = face_detector.detectMultiScale(frame, 1.3)
        for (x, y, w, h) in FACES:
            face = frame[y:y+h, x:x+w]
            frame[y:y+h, x:x+w] = cv2.flip(face, 0)
        
        k = cv2.waitKey(2)
        if k == 48: # k == ord("0")
            current_state = 0
    
    elif k == 27 or current_state == 27: # k == ord("esc")
        break
    
    else:
        pass
    
    cv2.imshow("Advanced Webcam", frame)