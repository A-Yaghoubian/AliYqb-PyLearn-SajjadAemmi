import argparse
from tensorflow.keras.models import load_model
import numpy as np
import cv2

parser = argparse.ArgumentParser(description='Fashion Mnist dataset - Ali Yaghoubian')
parser.add_argument('--input', type=str, help='image PATH', default='../data/example.png')
parser.add_argument('--model', type=str, help='MLP or CNN', default='CNN')
args = parser.parse_args()

if args.model == 'MLP':
    model = load_model('../models/fashionmnist_mlp.h5')
elif args.model == 'CNN':
    model = load_model('../models/fashionmnist_cnn.h5')

img = cv2.imread(args.input)
img = cv2.resize(img, (28, 28))
img = cv2.cvtColor(img, (img, cv2.COLOR_BGR2GRAY))
img = img / 255.0
img = img.reshape(28, 28, 1)

result = np.argmax(model.predict(img))
print(result)