import re

at_regex = re.compile(r'.at')
# ○atにマッチ（flagはlatとしてマッチする）
print(at_regex.findall('The cat in the hat sat on th flat mat.'))

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Al Last Name: Sweigart')
# Alを出力
print(mo.group(1))
# Sweigartを出力
print(mo.group(2))

NEW_LINE_TEXT = 'Serve the public trust. \n Protect the innocent \n Uphold the law.'
no_newline_regex = re.compile('.*')
# ~ trust. までを出力
print(no_newline_regex.search(NEW_LINE_TEXT).group())
new_line_regex = re.compile('.*', re.DOTALL)
# 改行コードを含めて全文表示
print(new_line_regex.search(NEW_LINE_TEXT).group())

