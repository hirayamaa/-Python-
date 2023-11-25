import time


def calc_prod():
    product = 1
    for i in range(1, 100000):
        product = product + i
    return product


start_time = time.time()
prod = calc_prod()
end_time = time.time()
print(f'計算結果は{prod}です')
print(f'計算時間は{end_time - start_time}秒でした')

# 現在時刻を文字列で取得
print(time.ctime())

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)
