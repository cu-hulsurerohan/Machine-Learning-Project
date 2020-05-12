# resizing images using bilinar interpolation

from PIL import Image
import numpy as np
from os import listdir
src = "F:/Processed Data/"
destination = "F:/Processed Data - 256/"

folders = listdir(src)

for folder in folders:
    files = listdir(src+folder)
    for file in files:
        img = Image.open(src+folder+"/"+file)
        img = img.resize((256, 256), Image.BICUBIC)
        img.save(destination+folder+"/"+file)