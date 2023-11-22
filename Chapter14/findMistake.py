import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]

for i, row in enumerate(sheet.getRows()):
    # 1行目は見出しのため検査しない
    if i == 0:
        continue
    # 行のすべてが空白の場合、終了
    if row[0] == '' and row[1] == '' and row[2] == '':
        break
    per_jar = int(row[0])
    jars = int(row[1])
    total = int(row[2])
    # 計算式が間違っている場合
    if total != per_jar * jars:
        print(f'{i+1}行目に間違いがあります')
        print(f'誤：{total}, 正：{jars*per_jar}')
print('間違いチェックが完了しました')
