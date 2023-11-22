import ezsheets

# 13章で使用したエクセルファイルをアップロードする
# ss = ezsheets.upload('../Chapter13/produceSales.xlsx')
# 上記でアップロードしたファイルを読み込む
ss = ezsheets.Spreadsheet('1lIcckxAxwjjQLJgnsVjaMyk8PWh6lgqJqQak3OqbUPs')
sheet = ss[0]
# 1行目の値のリストを表示
print(sheet.getRow(1))
print(sheet.getColumn(1))
column1 = sheet.getColumn(1)
for i, value in enumerate(column1):
    # Pythonのリストを大文字化する「
    column1[i] = value.upper()
# A列全体を１回のリクエストで更新
sheet.updateColumn(1, column1)

# シートの行数、列数を取得する
print(sheet.rowCount)
print(sheet.columnCount)
# 列数を変更する
sheet.columnCount = 4
