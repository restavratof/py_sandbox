import cv2 as cv
import img_utils as iu

"""
Here I'm doing the following:
 - resizing big image to small one.
 - copy image and save with gray scale 
"""

in_dir = '../_in'
img = 'pic1.jpg'
in_img = f'{in_dir}/{img}'

out_height, out_width = (350, 500)
img1_name = 'for_gif_1.jpg'
img2_name = 'for_gif_2.jpg'


# --------------------------------------------------------
# read
img = cv.imread(in_img)


res = cv.resize(img, (out_height, out_height), interpolation=cv.INTER_LINEAR)
iu.image_show(res)
iu.image_save(image=res, img_name=img1_name)

res_gray = iu.turn_to_grayscale(res)
iu.image_show(res_gray)
iu.image_save(image=res_gray, img_name=img2_name)
