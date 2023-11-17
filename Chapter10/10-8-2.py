import os
from pathlib import Path


def print_big_file(path):
    count = 0
    for foldername, subfolders, filenames in os.walk(path):
        folder_path = Path(foldername)
        for filename in filenames:
            # 100MB以上のファイル容量の場合出力
            if os.path.getsize(folder_path / filename) >= 100000000:
                print(folder_path / filename)
                count += 1
    print(f'{count}ファイル見つかりました')


p = Path.home() / 'Downloads'
print_big_file(p)
