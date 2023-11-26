import bs4
import requests
import os
from pathlib import Path

# Xkcdからランダムに画像をダウンロードする
comic_path = Path.home() / 'Documents/xkcd'
os.makedirs(comic_path, exist_ok=True)
url = 'https://c.xkcd.com/random/comic/'
res = requests.get(url)
res.raise_for_status()
bs = bs4.BeautifulSoup(res.text, 'html.parser')
comic_img = bs.select('#comic img')
if not comic_img:
    print('')
else:
    comic_url = 'https:' + comic_img[0].get('src')
    res = requests.get(comic_url)
    res.raise_for_status()
    comic_file = open(os.path.join(comic_path, os.path.basename(comic_url)), 'wb')

    for chunk in res.iter_content(100000):
        comic_file.write(chunk)
    comic_file.close()
