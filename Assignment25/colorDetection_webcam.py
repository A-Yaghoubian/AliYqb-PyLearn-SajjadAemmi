import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam_size = (640, 480)
text = ''
output = cv2.VideoWriter("colorDetection.mp4", cv2.VideoWriter_fourcc(*'MJPG'), 5.0, cam_size)

while(True):
    ret, frame = cam.read()
    if not ret:
        break
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rows, cols = frame.shape
    
    rec = frame[180 : 300, 250 : 370]
    frame[180:300, 245:250] = 0
    frame[180:300, 370:375] = 0
    frame[175:180, 245:375] = 0
    frame[300:305, 245:375] = 0 
    
    filter = np.ones((19, 19)) / 361  
    
    # for i in range(181, 299):
    #     for j in range(251, 369):
    #         x += 1
    #         final += frame[i, j]
    
    # for i in range(9, rows - 9):
    #     for j in range(9, cols - 9):
    #         if 305 >= i >= 175 and 375 >= j >= 245:
    #             pass
    #         else:
    #             small_img = frame[i - 9 : i + 10, j - 9 : j + 10]
    #             small_img_1d = small_img.reshape(361)
    #             small_img_1d_sorted = np.sort(small_img_1d)
    #             frame[i, j] = small_img_1d_sorted[180]
    
    frame = cv2.filter2D(frame, -1, filter, borderType=cv2.BORDER_CONSTANT)
    frame[180 : 300, 250 : 370] = rec
    
    if 0 <= np.average(rec) < 50:
        text = "black"
    elif 50 <= np.average(rec) < 120:
        text = "gray"
    elif 120 <= np.average(rec) <= 255:
        text = "white"
    
    cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 255, 255), 1)
    
    output.write(frame)
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
output.release()
cam.release()
cv2.destroyAllWindows()
