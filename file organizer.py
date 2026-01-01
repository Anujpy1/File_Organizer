import os
import shutil

path = input('Please enter the path of the folder: ')

if (not os.path.exists(fr'{path}\Images')):
    os.mkdir(fr'{path}\Images')

if (not os.path.exists(fr'{path}\Documents')):
    os.mkdir(fr'{path}\Documents')

if (not os.path.exists(fr'{path}\Videos')):
    os.mkdir(fr'{path}\Videos')

if (not os.path.exists(fr'{path}\Others')):
    os.mkdir(fr'{path}\Others')

files = os.listdir(fr'{path}')

for file_name in files:
    file_path = os.path.join(path, file_name)    
    
    if os.path.isdir(file_path):
        continue

    elif file_name.endswith(('.png', '.jpg')):
        shutil.move(file_path, os.path.join(path, 'Images', file_name))
    
    elif file_name.endswith(('.pdf', '.c')):
        shutil.move(file_path, os.path.join(path, 'Documents', file_name))
    
    elif file_name.endswith('.mp4'):
        shutil.move(file_path, os.path.join(path, 'Videos', file_name))
    
    else:
        shutil.move(file_path, os.path.join(path, 'Others', file_name))
