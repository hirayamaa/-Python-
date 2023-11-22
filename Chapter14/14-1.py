import ezsheets

# スプレッドシートの読み込み
# ss = ezsheets.Spreadsheet('12oLpPd2RCjJLLPL2Wr4WiiTLcBuOiddgns92g7DwsxE')
# print(ss.title)

# スプレッドシートの新規作成
# ss = ezsheets.createSpreadsheet('Title of My Spreadsheet')
# print(ss.title)

# スプレッドシートの属性
ss = ezsheets.Spreadsheet('1MQltwnsDjoR5Xoyc5FBqpp3UxbZWblB5fJf_XhZgkS8')
print(ss.title)
print(ss.id)
print(ss.url)
# シート名一覧
print(ss.sheetTitles)
# シートオブジェクトの一覧
print(ss.sheets)
print(ss[0])
# シート名でもアクセス可能
print(ss['Students'])
# シートの削除（権限がなければ不可能）
# del ss[0]
# スプレッドシートをエクセル形式でダウンロード
# ss.downloadAsExcel()

