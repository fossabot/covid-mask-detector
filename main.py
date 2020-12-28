import os
import re

for folder in ['train', 'valid' , 'test']:
    file_list = os.listdir(f'./{folder}')
    for file in file_list:
        if not file.endswith('.txt'):
            continue
        with open(f'./{folder}/{file}', 'r+') as f:
            lines = f.read()
            replaced = re.sub(r'0(?=\s\d+\.\d+){4}', '1', lines)
            replaced = re.sub(r'2(?=\s\d+\.\d+){4}', '0', lines)
            f.seek(0)
            f.write(replaced)
            f.truncate()

            