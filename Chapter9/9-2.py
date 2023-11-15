from pathlib import Path

p = Path('hello.txt')
p.write_text('Hello World')

# hello.txtを開いてFileオブジェクトを取得する
hello_file = open('hello.txt')
print(hello_file.read())

sonnet_file = open('sonnet29.txt')
print(sonnet_file.readlines())

# ファイルの書き込み
bacon_file = open('bacon.txt', 'w')
bacon_file.write('ベーコン！\n')
bacon_file.close()
bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

bacon_file = open('bacon.txt')
print(bacon_file.readlines())
