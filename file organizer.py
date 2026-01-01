import os
import shutil

path = input('Please enter the path of the folder: ')

if (not os.path.join(path, 'Images')):
    os.mkdir(os.path.join(path, 'Images'))

if (not os.path.join(path, 'Documents')):
    os.mkdir(os.path.join(path, 'Documents'))

if (not os.path.join(path, 'Videos')):
    os.mkdir(os.path.join(path, 'Videos'))

if (not os.path.join(path, 'Others')):
    os.mkdir(os.path.join(path, 'Others'))

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
