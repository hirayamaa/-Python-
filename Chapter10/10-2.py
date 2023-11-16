import os
from pathlib import Path

p = Path('')

for foldername, subfolders, filenames in os.walk(p):
    print(f'現在のディレクトリは{foldername}')
    for subfolder in subfolders:
        print(f'{foldername}のサブディレクトリ{subfolder}')
    for filename in filenames:
        print(f'{foldername}内のファイル{filename}')

