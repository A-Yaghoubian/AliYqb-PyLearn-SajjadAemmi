import cv2
from tensorflow.keras.models import load_model
import numpy as np

class Animal_Detector_CNN:
    def __init__(self):
        self.model = load_model("E:\programming\PyLearn-SajjadAemmi\Assignment44\Animal_Detector\model\\animalDetector_model.h5")
        self.width = self.height = 224
        
    def predict(self, image_path):        
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # cv2_format != tensorflow_format
        image = cv2.resize(image, (self.width, self.height))
        # normalize
        image = image / 255 
        # batch size
        image = image.reshape(1, self.width, self.height, 3) # 3d -> 4d
        
        result = self.model.predict(image)
        pred = np.argmax(result)
        
        if pred == 0:
            answer = "Bee 🐝"
        elif pred == 1:
            answer = "Koala 🐨"
        elif pred == 2:
            answer = "Crocodile 🐊"
        elif pred == 3:
            answer = "Crow 🐧"
        elif pred == 4:
            answer = "Zebra 🦓"
            
        return answer