import os
import shutil
from pathlib import Path

p = Path('textFiles')
Path(p / 'spam.txt').write_text('SPAM')
Path(p / 'some_folder').mkdir()
# spam.txtをsome_folder内にコピーする
shutil.copy(p / 'spam.txt', p / 'some_folder')
# spam.txtをsome_folder内にファイル名をeggs.txtとしてコピーする
shutil.copy(p / 'spam.txt', p / 'some_folder/eggs.txt')
# some_folder配下の全てのファイルをコピーしてspam_backupというフォルダーを作成
shutil.copytree(p / 'some_folder', p / 'spam_backup')
