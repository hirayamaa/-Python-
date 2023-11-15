import re

# テキストを読み込み中身の文章を取得する
read_file = open('replace.txt')
replace_text = read_file.read()
# 新しいファイルに書き込む文章

sentence_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
matches = sentence_regex.findall(replace_text)

# ユーザに入力してもらった文章に置き換えていく処理
for match in matches:
    print('Enter a ', end='')
    rep = input(match.lower() + ': ')
    replace_text = replace_text.replace(match, rep, 1)

# 置き換え後のファイルを保存する
write_file = open('replaced.txt', 'w')
write_file.write(replace_text)
read_file.close()
write_file.close()

