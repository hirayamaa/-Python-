import time

print('Enterを押すと開始します。その後、Enterを押せば経過時間を表示します。'
      'Ctrl-Cで終了します')
# Enterを押すと開始
input()
print('スタート')
# プログラムと最初のラップの開始時間
start_time = time.time()
last_time = start_time
lap_num = 1

# ラップタイムを計測する
try:
    while True:
        input()
        now = time.time()
        lap_time = round(now - last_time, 2)
        total_time = round(now - start_time, 2)
        print(f'ラップ #{lap_num}: {total_time} ({lap_time})', end='')
        lap_num += 1
        # ラップタイムをリセット
        last_time = now
except KeyboardInterrupt:
    print('\n終了')

