import time
import subprocess

time_left = 60
while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left -= 1

# カウントダウン後に音声ファイルを再生する
subprocess.run(['open', 'alarm.wav'])
