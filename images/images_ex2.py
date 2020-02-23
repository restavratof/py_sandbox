from PIL import Image, ImageFilter
import os

FILENAME = 'testpic.jpg'

#Read image
im = Image.open(FILENAME)
#Display image
# im.show()

####################################################
#Applying a filter to the image
action = 'sharpen'
in_name, in_ext = os.path.splitext(FILENAME)
OUT_FILENAME = in_name + action + in_ext

im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
im_sharp.save(OUT_FILENAME, 'JPEG')

####################################################
#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()
print('R:{}\nG:{}\nB:{}'.format(r,g,b))

####################################################
#Viewing EXIF data embedded in image
exif_data = im._getexif()
print('EXIF:{}'.format(exif_data))

import cv2 as cv
print(cv.__version__)