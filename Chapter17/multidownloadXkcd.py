import time

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)


def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        print(f'ページをダウンロード中 https://xkcd.com/{url_number}...')
        res = requests.get(f'https://xkcd.com/{url_number}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # コミックの画像のURLを見つける
        comic_elem = soup.select('#comic img')
        if not comic_elem:
            print('コミック画像が見つかりませんでした')
        else:
            comic_url = 'https://' + comic_elem[0].get('src')
            print(f'画像をダウンロード中 {comic_url}...')
            res = requests.get(comic_url)
            res.raise_for_status()
            # 画像を保存する
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()
        time.sleep(20)


# Threadオブジェクトを生成して開始する
download_threads = []
for i in range(0, 140, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1
    download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()

# すべてのスレッドが終了するのを待つ
for download_thread in download_threads:
    download_thread.join()
print('完了')
