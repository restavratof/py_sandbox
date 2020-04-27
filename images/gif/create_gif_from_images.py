import imageio
import os

# https://note.nkmk.me/en/python-pillow-gif/

result_gif = 'mytest.gif'

img_dir = '/home/dfashchanka/PycharmProjects/py_sandbox/images/gif/in'
images_in = os.listdir(img_dir)
images_out = list()
# print(images)

for img in images_in:
    images_out.append(imageio.imread(f'{img_dir}/{img}'))
imageio.mimsave(result_gif, images_out)
