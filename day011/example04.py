"""
example04 - 

Author: kaiby
Date: 2024/1/8 9:49
"""
import utils

extension_name = utils.get_file_type('adsfad.txt.exe', is_containt_dot=False)
print(extension_name)
extension_name = utils.get_file_type('adsfad.py', is_containt_dot=True)
print(extension_name)

