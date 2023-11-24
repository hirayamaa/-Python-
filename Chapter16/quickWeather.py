import json
import requests
import sys

if len(sys.argv) < 2:
    print('Usage quickWeather.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])

APPID = 'a0f683f2001b68206732aeeca5ce73f3'
# OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
url = ('https://api.openweathermap.org/data/2.5/forecast?'
       + f'q={location}&appid={APPID}')
response = requests.get(url)
response.raise_for_status()

# JSONデータからPython変数に読み込む
weather_data = json.loads(response.text)

# 確認用ファイルに書き込む
# import pprint
# file = open('Chapter16/weather_Tokyo.txt', 'w')
# file.write(pprint.pformat(weather_data))
# file.close()

w = weather_data['list']
print(f'{location}の現在のお天気:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print(f'明日のお天気:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print(f'明後日のお天気:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
