import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from mtcnn import MTCNN

class Detector:
    def __init__(self):
        self.model = load_model('E:\programming\PyLearn-SajjadAemmi\Assignment46\Face Mask Detection\Model\FaceMask-MobileNetV2.h5')
        self.face_detector = MTCNN()
        
    def detect(self, image):
        RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        Faces = self.face_detector.detect_faces(RGB_image)
        width = height = 224
        
        if Faces:
            for face in Faces:
                x, y, w, h = face["box"]
                
                img = RGB_image[y:y+h, x:x+w]
                resized_image = cv2.resize(img, (width, height))
                resized_image = resized_image / 255.0
                reshaped_image = resized_image.reshape(1, width, height, 3)
                
                result = np.argmax(self.model.predict(reshaped_image))
                
                if result == 0:
                    result = "With Mask ✔"
                    color = (0, 255, 0)
                elif result == 1:
                    result = "Without Mask ❌"
                    color = (0, 0, 255)
                
                cv2.rectangle(image, (x, y), (x+w, y+h), color, 3)
                cv2.putText(image, result, (x, y-15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, color, 2)
                
            return image, True
        
        else:
            return image, False
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.detector = Detector()
        
        self.ui = loader.load('E:\programming\PyLearn-SajjadAemmi\Assignment46\Face Mask Detection\Inference\main.ui', None)
        self.ui.show()
        self.webcam()
    
    def webcam(self):
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            final_frame, y_pred = self.detector.detect(frame)
            
            if y_pred == True:
                RGB_frame = cv2.cvtColor(final_frame, cv2.COLOR_BGR2RGB)
            elif y_pred == False:
                RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
            RGB_frame = cv2.resize(RGB_frame, (600, 500))
            image = QImage(RGB_frame, RGB_frame.shape[1], RGB_frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)    
            self.ui.camera_label.setPixmap(pixmap)
           
            if cv2.waitKey(1) == ord("q"):
                break
            
        cap.release()
        cv2.destroyAllWindows()
            
    
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()