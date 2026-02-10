"""
example10 - 

Author: kaiby
Date: 2024/1/16 15:51
"""
import shutil
import os

print(shutil.which('python'))
# shutil.copy('winter.jpg', 'winter_copy.jpg')

# shutil.move('winter_copy.jpg', 'winter_move.jpg')

file_list = os.listdir()
for file in file_list:
    print(file, os.path.isfile(file), os.path.isdir(file))
