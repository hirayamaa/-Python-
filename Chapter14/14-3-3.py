import ezsheets
# シートのコピーを作成する
ss1 = ezsheets.createSpreadsheet('First Spreadsheet')
ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')

ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
# ss1のシート1をss2へコピー
ss1[0].copyTo(ss2)
print(ss2.sheetTitles)
