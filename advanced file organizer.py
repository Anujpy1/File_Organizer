import os
import shutil

path = input('Please enter the path of the folder: ')

folder = (('Images', r'Documents\pdf files', r'Documents\Word files', r'Documents\Excel files', r'Documents\PPT files', 'Videos', r'Programs\Python files', r'programs\Java files', r'programs\HTML files', r'programs\C files', 'Music', 'Others'))
for file in folder:
    os.makedirs(os.path.join(path, file), exist_ok=True)

files = os.listdir(fr'{path}')

for file_name in files:
    file_path = os.path.join(path, file_name)    
    
    if os.path.isdir(file_path):
        continue

    elif file_name.endswith(('.png', '.jpg')):
        shutil.move(file_path, os.path.join(path, folder[0], file_name))
    
    elif file_name.endswith('.pdf'):
        shutil.move(file_path, os.path.join(path, folder[1], file_name))

    elif file_name.endswith('.docx'):
        shutil.move(file_path, os.path.join(path, folder[2], file_name))

    elif file_name.endswith('.xlsx'):
        shutil.move(file_path, os.path.join(path, folder[3], file_name))

    elif file_name.endswith('.pptx'):
        shutil.move(file_path, os.path.join(path, folder[4], file_name))
    
    elif file_name.endswith('.mp4'):
        shutil.move(file_path, os.path.join(path, folder[5], file_name))

    elif file_name.endswith('.py'):
        shutil.move(file_path, os.path.join(path, folder[6], file_name))

    elif file_name.endswith('.j'):
        shutil.move(file_path, os.path.join(path, folder[7], file_name))

    elif file_name.endswith(('.html', '.css', '.js')):
        shutil.move(file_path, os.path.join(path, folder[8], file_name))

    elif file_name.endswith('.c'):
        shutil.move(file_path, os.path.join(path, folder[9], file_name))

    elif file_name.endswith(('wpl', '.mp3')):
        shutil.move(file_path, os.path.join(path, folder[10], file_name))
    
    else:
        shutil.move(file_path, os.path.join(path, folder[11], file_name))