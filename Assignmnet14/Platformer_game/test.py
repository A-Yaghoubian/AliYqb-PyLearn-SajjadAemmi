import imageio
import os

images = []

for file_name in sorted(os.listdir('gif_images')):
    print(file_name)
    img = imageio.imread('gif_images' + '/' + file_name)
    images.append(img)

imageio.mimsave('move.gif', images)