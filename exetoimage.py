# converting .exe files to images follows et. Natraj algorithm

import os
from math import log
import numpy as np
from PIL import Image


bytes_dir = "F:/benign_bytes/"
image_dir = "F:/benign_images/"
files = os.listdir(bytes_dir)

def saveimg(array, name):
    if array.shape[1] != 16:
        assert (False)
    b = int((array.shape[0] * 16) ** (0.5))
    b = 2 ** (int(log(b) // log(2)) + 1)
    a = int(array.shape[0] * 16 // b)
    print(a, b)
    array = array[:a * b // 16, :]

    array = np.reshape(array, (a, b))
    print(array.shape)

    # array = np.uint8(array)
    # print(array)
    # array.resize((256,256))

    im = Image.fromarray(np.uint8(array), 'L')
    im.save(image_dir+name.split('.')[0]+'.png')
    return

c = 0
for file in files:
    array = []
    print(c)
    c+=1
    with open(bytes_dir+file, "rb") as f:
        if os.path.isfile(image_dir+file.split('.')[0]+'.png'):
            print('Image already exists')
            continue

        print(file)
        byte = f.read().hex().upper()
        hexlist = list(map(''.join, zip(*[iter(byte)]*2)))
        hexlist = [int(i,16) if i != '??' else 0 for i in hexlist]
        for x in range(0, len(hexlist), 16):
            array.append(hexlist[x:x+16])
        length = max(map(len, array))
        array = np.array([xi + [0] * (length - len(xi)) for xi in array])
        saveimg(np.array(array), file)
        del array
        del hexlist
        del byte
        f.close()

    print("")
