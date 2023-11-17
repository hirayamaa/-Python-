import os
from pathlib import Path
import shutil


# pathのディレクトリ配下のextに一致する拡張子のファイルをディレクトリにコピーする
def copy_images(path, ext):
    number = 1
    while True:
        # コピー先のフォルダ名(例：copy_jpg_1)
        copy_folder_name = f'copy_{ext[1:]}_{number}'
        if not os.path.exists(copy_folder_name):
            break
        number += 1

    # コピー先のフォルダを作成
    Path.mkdir(path / copy_folder_name)
    for foldername, subfolders, filenames in os.walk(path):
        # コピー対象のファイルを探す
        print(f'{foldername}を探索中')
        for filename in filenames:
            print(filename)
            if filename.endswith(ext):
                shutil.copy(Path(foldername) / filename, path / copy_folder_name)


p = Path.cwd()
copy_images(p, '.txt')
