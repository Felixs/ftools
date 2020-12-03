import sys
import os

if len(sys.argv) != 2:
    print('Usage: python sort_folder.py [folder]')
    sys.exit(1)

folder = sys.argv[1]
os.chdir(folder)

print(folder)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(files)

for file in files:

    extention = file.split('.')[-1]
    if extention == file:
        print(f'No File Extentions for {file}')
        continue
    if not os.path.exists(f'./{extention}'):
        os.makedirs(extention)

    os.replace(file, f'{extention}/{file}')
