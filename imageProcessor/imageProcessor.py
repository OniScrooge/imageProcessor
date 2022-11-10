from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):                       # Opens file in listed path /imgs for use
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L') # Sharpens and covnerts image into grayscale

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)              # Sets edit for contrast enhancing
    edit = enhancer.enhance(factor)                     # Which is done here by the predertermined factor

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')