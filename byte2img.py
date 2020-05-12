# For converting bytes to images follows et Natraj algorithm

import os
from math import log
import numpy as np
from PIL import Image

bytes_dir = ["F:/train_bytes/Gatak/", "F:/train_bytes/Simda/", "F:/train_bytes/Tracur/", "F:/train_bytes/Vundo/", "F:/train_bytes/Obfuscator.ACY/"]
image_dir = ["F:/train_images/Gatak/", "F:/train_images/Simda/", "F:/train_images/Tracur/", "F:/train_images/Vundo/", "F:/train_images/Obfuscator.ACY/"]

def saveimg(array, name, image_dir):
    print(name)
    if array.shape[1] != 16:
        assert (False)
    b = int((array.shape[0] * 16) ** (0.5))
    b = 2 ** (int(log(b) // log(2)) + 1)
    a = int(array.shape[0] * 16 // b)
    print(a, b)
    array = array[:a * b // 16, :]

    array = np.reshape(array, (a, b))
    print(array.shape)
    print("")

    im = Image.fromarray(np.uint8(array), 'L')
    im.save(image_dir+name.split('.')[0]+'.png')

for src, dst in zip(bytes_dir, image_dir):
    files = os.listdir(src)
    c = 0
    for cc, x in enumerate(files):
        f = open(src+x)
        array = []
        c += 1
        for line in f:
            xx = line.split()
            if len(xx) != 17:
                continue

            array.append([int(i, 16) if i != '??' else 0 for i in xx[1:]])
        saveimg(np.array(array), x, dst)
        del array
        f.close()

    print(c)