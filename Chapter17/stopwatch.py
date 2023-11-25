import time
import pyperclip

print('Enterを押すと開始します。その後、Enterを押せば経過時間を表示します。'
      'Ctrl-Cで終了します')
# Enterを押すと開始
input()
print('スタート')
start_time = time.time()
total_time = 0
lap_num = 1
copy_list = []

while True:
    try:
        input()
        start_time = round(time.time() - start_time, 2)
        total_time = round(total_time + start_time, 2)
        s = f'ラップ #{lap_num:2}: {total_time:5.2f} ({start_time:5.2f})'
        print(s, end='')
        start_time = time.time()
        lap_num += 1
        copy_list.append(s)
    except KeyboardInterrupt:
        # 表示タイムをコピーする
        pyperclip.copy('\n'.join(copy_list))
        print('\nストップウォッチ終了')
