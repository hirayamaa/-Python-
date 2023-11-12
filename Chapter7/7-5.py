import re

PHONE_NUMBER_TEXT = 'Cell: 415-555-9999 Work:212-555-0000'

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# ['415-555-9999', '212-555-0000']が出力される（リスト）
print(phone_num_regex.findall(PHONE_NUMBER_TEXT))

# [('415', '555', '9999'), ('212', '555', '0000')]が出力される（タプルのリスト）
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phone_num_regex.findall(PHONE_NUMBER_TEXT))

