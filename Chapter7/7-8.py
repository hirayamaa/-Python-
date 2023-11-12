import re

begins_with_hello = re.compile(r'^Hello')
# 先頭のためマッチする
print(begins_with_hello.search('Hello world!'))
# マッチしない（Noneを出力）
print(begins_with_hello.search('He said Hello'))

ends_with_number = re.compile(r'\d$')
# 末尾が数値のためマッチする
print(ends_with_number.search('Your number is 42'))
# マッチしない
print(ends_with_number.search('Your number is forty two.'))

whole_string_is_num = re.compile(r'^\d+$')
# 全体が数値のためマッチする
print(whole_string_is_num.search('0123456789'))
# 英字やスペースがあるためマッチしない
print(whole_string_is_num.search('012345xyz6789'))
print(whole_string_is_num.search('012 34567 89'))
