import re

num_regex = re.compile(r'^\d{1,3}(,\d{3})*$')
test_datas = ['42', '1,234', '6,368,745', '12,34,567', '1345']
for test_data in test_datas:
    mo = num_regex.search(test_data)
    if mo is None:
        print(test_data + 'は３桁ごとのカンマ形式ではありません')
    else:
        print(mo.group() + 'は３桁ごとのカンマ形式です')

