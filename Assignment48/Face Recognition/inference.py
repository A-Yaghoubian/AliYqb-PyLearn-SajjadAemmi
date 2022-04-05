import argparse
import numpy as np
import cv2
from facerecognition import AliNet

width = height = 224
PERSONS = ['Ali Khamenei', 'Angelina Jolie', 'Barak Obama', 'Behnam Bani', 'Donald Trump', 'Emma Watson', 'Han Hye Jin',
           'Kim Jong Un', 'Leyla Hatami', 'Lionel Messi', 'Michelle Obama', 'Morgan Freeman', 'Queen Elizabeth', 'Scarlett Johansson']

parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str, default='sample.jpg', help='Image Path')
parser.add_argument('--weights', type=str, default='faceRecognition', help='Weights Path')
args = parser.parse_args()

model = AliNet()
model.load_weights(args.weights)

image = cv2.imread(args.input_image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (width, height))
image = image / 255.0
image = image[np.newaxis, ...]

result = np.argmax(model.predict(image))
print(PERSONS[result])