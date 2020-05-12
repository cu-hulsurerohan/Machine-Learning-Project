import os
from os import listdir

# listdir is used to list files inside the folder
def scandir(path):
    for filename in listdir(path):
        if filename.endswith('.asm'):
            try:
                os.remove(path+filename)
                ## os.remove - deletes file specified in the path
            except OSError:
                print("Error While handling file", filename)
                break

    print("Done")

# to rename files according to categories
def renme(path, key):
    count = 1
    for filename in listdir(path):
        if filename.endswith('.bytes'):
            try:
                os.rename(path+filename, path+key+" "+str(count)+'.bytes')
                ## os.rename - renames files specified in path
                count += 1
            except OSError:
                print("Error while renaming file",filename)
    print("Done ", key, count )
# scandir("F:/train_bytes/")

# created a dictionary for classes/categories
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

dir = "F:/train_bytes/"

for key in folders:
    folder_name = folders[key]
    path = dir+folder_name+'/'
    renme(path, folder_name)

