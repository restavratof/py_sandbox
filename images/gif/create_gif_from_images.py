from PIL import Image
import os

# https://note.nkmk.me/en/python-pillow-gif/

in_dir = '../_in'
out_dir = '../_out'
result_gif = f'{out_dir}/my_test.gif'
img_prefix = 'for_gif_'
images_raw = os.listdir(in_dir)
print(f'1: {images_raw}')
# Filter required images' names and create a list of images
images = [Image.open(f'{in_dir}/{x}') for x in images_raw if str(x).startswith(img_prefix)]
print(f'2: {images}')
# To show images with OS default software
# for im in images:
#    im.show()

images[0].save(result_gif,
               save_all=True, append_images=images[1:], optimize=False, duration=400, loop=0)

"""
TODO: Investigate the following 
When I tried to save gif with images in different modes. In the following order (RGB, L) 
        -> It failed with error NoneType palette 
As a prompt solution I just renamed files to appear in reversed order (L, RGB) -> No issue

Some discussions I found there: https://github.com/python-pillow/Pillow/issues/1717
"""
