import cv2

cam = cv2.VideoCapture(0)
_, f = cam.read()
final_image = f

cam_size = (640, 480)
output = cv2.VideoWriter("timewrapscan.mp4", cv2.VideoWriter_fourcc(*'MJPG'), 20.0, cam_size)

r = 0
while(True):
    ret, frame = cam.read()
    if not ret:
        break
    
    rows, cols, _ = frame.shape
    
    frame[r : r + 3, :] = (200, 0, 0)
    try:
        final_image[r - 3 : r, :] = frame[r - 3 : r, :]
    except:
        pass
    
    frame[ : r, :] = final_image[ : r, :]
    
    output.write(frame)
    cv2.imshow("frame", frame)
    r += 1
    
    if r > rows:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.imwrite('final_image.jpg', final_image)
output.release()
cam.release()
cv2.destroyAllWindows()