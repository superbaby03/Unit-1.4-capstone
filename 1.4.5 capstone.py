import PIL
from PIL import ImageColor
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt
import os.path
import numpy as np
image = Image.open('canceruk.jpg')

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'canceruk.jpg')
img = plt.imread('canceruk.jpg')

fig, axes = plt.subplots(1, 1)
axes.imshow(image, interpolation='none')
fig.show()

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'canceruk2.jpg')
img = plt.imread('canceruk2.jpg')

fig, axes = plt.subplots(1, 1)
axes.imshow(image, interpolation='none')
fig.show()

image = Image.open('canceruk.jpg')
logo = Image.open('canceruk2.jpg')
image_copy = image.copy()
image_copy.paste(logo, (9, 8))
image_copy.save('pasted_cancer.jpg')

image = Image.open('pasted_cancer.jpg')
greycale_image = image.convert('L')
greycale_image.save('greyscale_cancer.jpg')
