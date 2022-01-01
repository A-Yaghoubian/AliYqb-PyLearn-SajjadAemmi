import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam_size = (640, 480)
text = ''
# output = cv2.VideoWriter("colorDetection.mp4", cv2.VideoWriter_fourcc(*'MJPG'), 5.0, cam_size)

while(True):
    ret, frame = cam.read()
    if not ret:
        break
    
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rows, cols, _ = frame.shape
    
    rec = frame[180 : 300, 250 : 370]
    frame[180:300, 245:250] = 0
    frame[180:300, 370:375] = 0
    frame[175:180, 245:375] = 0
    frame[300:305, 245:375] = 0 
    
    filter = np.ones((19, 19)) / 361  
    
    frame = cv2.filter2D(frame, -1, filter, borderType=cv2.BORDER_CONSTANT)
    frame[180 : 300, 250 : 370] = rec
    
    blue = []
    green = []
    red = []
    for i in range(180, 300):
        for j in range(250, 370):
            b, g, r = frame[i, j]
            blue.append(b)
            green.append(g)
            red.append(r)
    
    if np.average(blue) < 70 and np.average(green) < 70 and np.average(red) < 70:
        text = "Black"
        
    elif np.average(blue) > 180 and np.average(green) > 180 and np.average(red) > 180:
        text = "White"
        
    elif np.average(blue) >= 180 and np.average(green) < 70 and np.average(red) < 70:
        text = "Blue"
        
    elif np.average(blue) < 70 and np.average(green) >= 180 and np.average(red) < 70:
        text = "Green"
        
    elif np.average(blue) < 70 and np.average(green) < 70 and np.average(red) >= 180:
        text = "Red"
        
    elif np.average(blue) < 180 and np.average(green) >= 180 and np.average(red) >= 180:
        text = "Yellow"
        
    elif np.average(blue) >= 180 and np.average(green) < 70 and np.average(red) >= 180:
        text = "Magenta"
        
    elif np.average(blue) >= 180 and np.average(green) >= 180 and np.average(red) < 70:
        text = "Cyan"
        
    elif 71 <= np.average(blue) < 180 and 71 <= np.average(green) < 180 and 71 <= np.average(red) < 180:
        text = "Gray"
    
    else:
        text = "None"
    
    cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 255, 255), 1)
    
    # output.write(frame)
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# output.release()
cam.release()
cv2.destroyAllWindows()