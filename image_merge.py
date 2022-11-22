import os
from PIL import Image

#path = '/home/thaycafe/images'
path = os.getcwd()
images = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.png']


for image in images:
    image = Image.open(image)
    print("-> Inserting background in PNG image:",image.filename)
    bg = Image.open('white_bg.jpg')
    bg.paste(image, (0, 0), image)


    image_path = 'images/' + image.filename.split(".")[0] + '.jpeg'
    print("\n-> Saving image in JPEG: ", image_path)
    bg.save(image_path, 'JPEG')
    print("\n-----------------------------------------------")
