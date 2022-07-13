import cv2
import img_utils as iu

in_dir = '../_in'
img = 'pic1.jpg'
in_img = f'{in_dir}/{img}'

# read
img = cv2.imread(in_img)

# show
# print(img)

# ----------------------------------
# to grayscale
gray_image = iu.turn_to_grayscale(img)
# show
iu.image_show(gray_image)
# iu.image_save(gray_image, f'gray_{img}')
