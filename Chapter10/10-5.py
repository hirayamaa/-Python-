import zipfile
import os
from pathlib import Path


# ディレクトリ全体を連番つきのZIPファイルにコピーする
def back_up_zip(folder):
    # ディレクトリ全体をZIPファイルにバックアップする
    folder = os.path.abspath(folder)
    # 既存のファイル名からファイル名の連番を決める
    number = 1
    while True:
        zip_filename = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1
    # ZIPファイルを作成する
    print(f'{zip_filename}を作成中')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    # ディレクトリ内のファイルを圧縮する
    new_base = os.path.basename(folder) + '_'
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'{foldername}を追加中・・・')
        backup_zip.write(foldername)
        for filename in filenames:
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print('終了しました')


# Chapter10内のファイルをZIP化
p = Path('')
back_up_zip(p)


