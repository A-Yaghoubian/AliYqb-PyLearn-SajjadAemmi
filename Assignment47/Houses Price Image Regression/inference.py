import os
import numpy as np
from tensorflow.keras.models import load_model
import cv2

model = load_model('cnn-HousePrices.h5')
images = []

for image in os.listdir('test'):
    img = cv2.imread('test/' + image)
    img = cv2.resize(img, (32, 32))
    images.append(img)

img4 = np.zeros((64, 64, 3), dtype="uint8")
img4[0:32, 0:32] = images[0]
img4[0:32, 32:64] = images[1]
img4[32:64, 32:64] = images[2]
img4[32:64, 0:32] = images[3]

img4 = img4/255
img4 = img4.reshape(1, 64, 64, 3)
pred = model.predict([img4])
print('Estimated Price: ', pred)