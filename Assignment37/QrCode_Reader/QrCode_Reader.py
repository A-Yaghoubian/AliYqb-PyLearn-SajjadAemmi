import cv2
from pyzbar.pyzbar import decode

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    well_frame = decode(frame)
    for i in well_frame:
        cv2.putText(frame, i.data.decode("utf-8"), (i.rect[0], i.rect[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("", frame)
    
    if cv2.waitKey(1) == ord("q"):
        break