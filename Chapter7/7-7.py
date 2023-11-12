import re

vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD. '))

TEST_TEXT = 'AAA abc あああ 8990 山田 ヤマダ'
# 半角英字
eng_regex = re.compile(r'[A-Za-z]')
print(eng_regex.findall(TEST_TEXT))
# 数字
num_regex = re.compile(r'[0-9]')
print(num_regex.findall('AAA abc あいうえお 987'))

# ひらがな
hiragana_regex = re.compile(r'[\u3040-\u309F]')
# ['あ', 'あ', 'あ']
print(hiragana_regex.findall(TEST_TEXT))

# カタカナ
katakana_regex = re.compile(r'[\u30A0-\u30FF]')
# ['ヤ', 'マ', 'ダ']
print(katakana_regex.findall(TEST_TEXT))

# 漢字
kanji_regex = re.compile(r'[\u4E00-\u9FFF]')
# ['山', '田']
print(kanji_regex.findall(TEST_TEXT))
