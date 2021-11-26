import cv2
import numpy as np

cam = cv2.VideoCapture(0)
text = ''

while(True):
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rows, cols = frame.shape
    final = 0
    
    frame[180:300, 245:250] = 0
    frame[180:300, 370:375] = 0
    frame[175:180, 245:375] = 0
    frame[300:305, 245:375] = 0  
    
    x = 0
    for i in range(181, 299):
        for j in range(251, 369):
            x += 1
            final += frame[i, j]
    
    for i in range(6, rows - 6):
        for j in range(6, cols - 6):
            if 305 >= i >= 175 and 375 >= j >= 245:
                pass
            else:
                small_img = frame[i - 6 : i + 7, j - 6 : j + 7]
                small_img_1d = small_img.reshape(169)
                small_img_1d_sorted = np.sort(small_img_1d)
                frame[i, j] = small_img_1d_sorted[84]
    
    if 0 <= (final / x) < 50:
        text = "black"
    elif 50 <= (final / x) < 120:
        text = "gray"
    elif 120 <= (final / x) <= 255:
        text = "white"
    
    cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.8, (255, 255, 255), 1)
    
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()