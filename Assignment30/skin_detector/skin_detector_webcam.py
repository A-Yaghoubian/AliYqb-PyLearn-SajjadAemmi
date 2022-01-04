import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while(True):
    ret, frame = cam.read()
    if not ret:
        break
    
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(frame_HSV)
    rows, cols, _ = frame.shape
    
    black_background = np.zeros((rows, cols), dtype='uint8')
    black_background_BGR = cv2.cvtColor(black_background, cv2.COLOR_GRAY2BGR)
    
    for i in range(rows):
        for j in range(cols):
            if 0 < H[i, j] < 20 and 35 < S[i, j] < 230 and 60 < V[i, j] < 250:
                black_background_BGR[i, j] = frame[i, j]
    
    cv2.imshow("frame", black_background_BGR)
    
    if cv2.waitKey(1) & 0xFF == ord('c'):
        cv2.imwrite('1.jpg', black_background_BGR)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()