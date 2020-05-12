# Script to lookup for benign .exe files

import os
import shutil


def recursive_walk(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        if subfolders:
            for subfolder in subfolders:
                recursive_walk(subfolder)
        # print('\nFolder: ' + folderName + '\n')
        for filename in filenames:
            if filename.endswith('.exe'):
                shutil.copy(folderName + "\\" + filename, dir_dst)
                # print(filename)


unallowed = ['desktop.ini', 'WindowsApps']
l = os.listdir("C:\\Program Files (x86)\\")
dir_dst = ("F:\\benign_bytes3")
for i in l:
    if i in unallowed:
        continue
    print('C:\\Program Files (x86)\\' + i)
    recursive_walk('C:\\Program Files (x86)\\' + i)
