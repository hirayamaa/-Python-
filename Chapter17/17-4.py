import datetime
import time

print(datetime.datetime.now())
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
print(datetime.datetime.fromtimestamp(time.time()))

halloween2019 = datetime.datetime(2019, 10, 31)
newyears2020 = datetime.datetime(2020, 1, 1)
oct31_2019 = datetime.datetime(2019, 10, 31)
print(halloween2019 == oct31_2019)
print(halloween2019 > newyears2020)
print(halloween2019 > newyears2020)
print(newyears2020 > halloween2019)
print(newyears2020 != oct31_2019)

print('############################')

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))

print('############################')

# timedeltaを使って1000日後を計算する
dt = datetime.datetime.now()
thousand_days = datetime.timedelta(days=1000)
print(dt + thousand_days)

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
about_thirty_years = datetime.timedelta(days=365 * 30)
print(oct21st - about_thirty_years)
print(oct21st - (2 * about_thirty_years))

print('############################')
# 日付のフォーマット
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

print('############################')
# 日付型の文字列のパース
print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
