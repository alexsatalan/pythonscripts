import sys
import os
from PIL import Image, ImageFilter

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

print(f'Your source folder is {source_folder} and your destination folder is {destination_folder}!')

for filename in os.listdir(source_folder):
    f = os.path.join(source_folder, filename)
    # checking the files present in the folder - debug message
    # if os.path.isfile(f):
    #     print(f)
    filename_without_ext = os.path.splitext(filename)[0]
    img = Image.open(f)
    img.save(f'{destination_folder}/{filename_without_ext}.png', 'png')
print('all done!')

    

