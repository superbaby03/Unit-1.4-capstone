import PIL
from PIL import ImageColor
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt
import os.path
image = Image.open('cancer.jpg')

fig, axes = plt.subplots(1, 1)
axes.imshow(image, interpolation='none')
fig.show()

image = Image.open('cancer.jpg')
greyscale_image = image.convert('L')
greyscale_image.save('greyscale_image.jpg')
