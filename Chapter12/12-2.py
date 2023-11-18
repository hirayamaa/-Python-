import requests

r = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(r))
print(r.status_code == requests.codes.ok)
print(len(r.text))

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print(f'問題あり:{exc}')
