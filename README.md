## Image Merge

Simple script for merging a png image with a white background image. In addition to merging, the image is converted and saved in JPEG format.


### Code details

```python
import os
from PIL import Image

## Defining the folder where the PNG images are located
#path = '/home/thaycafe/images'
path = os.getcwd()

## Filtering only files in PNG format
images = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.png']


for image in images:
    image = Image.open(image)
    print("-> Inserting background in PNG image:",image.filename)
    bg = Image.open('white_bg.jpg')

    ## Merging each PNG image in the folder with the white background image
    bg.paste(image, (0, 0), image)

    ## Defining the folder and file name where JPEG images will be saved
    image_path = 'images/' + image.filename.split(".")[0] + '.jpeg'
    print("\n-> Saving image in JPEG: ", image_path)

    ## Saving the image in JPEG
    bg.save(image_path, 'JPEG')
    print("\n-----------------------------------------------")

```
