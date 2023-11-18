import urllib.parse
import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # 引数の住所をリストとして受け取る
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
# 日本語の場合に文字化けを防ぐ
address = urllib.parse.quote(address)

webbrowser.open('https://www.google.com/maps/place/' + address)
