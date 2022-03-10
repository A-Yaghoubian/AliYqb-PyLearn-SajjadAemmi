import argparse
from tensorflow.keras.models import load_model
import numpy as np
import cv2

parser = argparse.ArgumentParser(description='CIFAR10 dataset - Ali Yaghoubian')
parser.add_argument('--input', type=str, help='image PATH', default='../data/example.png')
parser.add_argument('--model', type=str, help='MLP or CNN', default='CNN')
args = parser.parse_args()

if args.model == 'MLP':
    model = load_model('../models/cifar10_mlp.h5')
elif args.model == 'CNN':
    model = load_model('../models/cifar10_cnn.h5')

img = cv2.imread(args.input)
img = cv2.resize(img, (32, 32))
img = cv2.cvtColor(img, (img, cv2.COLOR_BGR2GRAY))
img = img / 255.0
img = img.reshape(32, 32, 3)

result = np.argmax(model.predict(img))
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
print(class_names[result])