import datetime
from pathlib import Path

# launchdの動作確認用のプログラム
f = open(Path.home() / 'Documents/python/time.txt', 'a')
date = datetime.datetime.now()
f.write(date.strftime('%Y/%m/%d %H:%M:%S') + '\n')
f.close()
