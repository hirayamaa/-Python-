import re
phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_number_regex.search('私の電話番号は415-555-4242です')

# 7.3.1 丸括弧を用いたグルーピング
# 415-555-4242を返す
print(mo.group(0))
# 415を返す
print(mo.group(1))
# 415-4242を返す
print(mo.group(2))
# ('415', '555-4242')を返す（タプル）
print(mo.groups())

print("################################")
# 7.3.2 「|」を用いたマッチ
hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey')
mo2 = hero_regex.search('Tina Fey and Batman')
# Batmanが出力される
print(mo1.group())
# Tina Feyが出力される
print(mo2.group())
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
# Batmobileが出力される
print(mo.group())
# mobileが出力される
print(mo.group(1))

print("################################")

BATMAN_TEXT = 'The Adventure of Batman'
BATWOMAN_TEXT = 'The Adventure of Batwoman'
BATWOWOWOMAN_TEXT = 'The Adventure of Batwowowoman'

# 7.3.3 疑問符を用いたマッチ
bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search(BATMAN_TEXT)
mo2 = bat_regex.search(BATWOMAN_TEXT)
# Batmanが出力される
print(mo1.group())
# Batwomanが出力される
print(mo2.group())

print("################################")

# 7.3.4 アスタリスクを用いたマッチ
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search(BATMAN_TEXT)
mo2 = bat_regex.search(BATWOMAN_TEXT)
mo3 = bat_regex.search(BATWOWOWOMAN_TEXT)
# Batmanが出力される
print(mo1.group())
# Batwomanが出力される
print(mo2.group())
# Batwowowomanが出力される
print(mo3.group())

print("################################")

# 7.3.5 プラスを用いたマッチ
bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search(BATWOMAN_TEXT)
mo2 = bat_regex.search(BATWOWOWOMAN_TEXT)
mo3 = bat_regex.search(BATMAN_TEXT)
# Batwomanが出力される
print(mo1.group())
# Batwowowomanが出力される
print(mo2.group())
# Trueが出力される
print(mo3 is None)
