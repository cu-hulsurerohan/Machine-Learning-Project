# Seggregate and prepare dataset

import os
import pandas as pd
import shutil


def move_files(filename, origin_folder, dest_folder):
    if os.path.exists(origin_folder+filename+".bytes"):
        shutil.move(origin_folder+filename+".bytes", dest_folder)
    else:
        print("already moved")
        return

label_csv = "F:/trainLabels.csv"
csv = pd.read_csv(label_csv)
df = pd.DataFrame(csv)
dictionary = df.set_index("Id")["Class"].to_dict()
dir = "F:/"
origin_folder = "F:/train_bytes/"

folders = dict()
folders[1] = "Ramnit"
folders[2] = "Lollipop"
folders[3] = "Kelihos_ver3"
folders[4] = "Vundo"
folders[5] = "Simda"
folders[6] = "Tracur"
folders[7] = "Kelihos_ver1"
folders[8] = "Obfuscator.ACY"
folders[9] = "Gatak"

for key in dictionary:
    category = dictionary[key]
    folder_name = folders[category]
    dest_dir = dir+folder_name+'/'
    move_files(key, origin_folder, dest_dir)
