from PIL import Image
import os

LOGO_FILENAME = 'logo.png'
# LOGO_FILENAME = 'logo_complete.png'

IN_FILENAME = '../_in/pic1.jpg'

in_name, in_ext = os.path.splitext(IN_FILENAME)
OUT_FILENAME = in_name + '_logo' + in_ext

print('OUT_FILENAME: {}'.format(OUT_FILENAME))


logoIm = Image.open(LOGO_FILENAME)
# print(logoIm)
logoWidth, logoHeight = logoIm.size
print('LOGO W:{}  H:{}\n'.format(logoWidth, logoHeight))

in_image = Image.open(IN_FILENAME)
# print(in_image)
width, height = in_image.size
print('IMAGE W:{}  H:{}'.format(width, height))


out_image = in_image.copy()
out_image.paste(logoIm, (0, height - logoHeight), logoIm)
out_image.save(OUT_FILENAME)
