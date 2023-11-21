import sys
from pathlib import Path
import openpyxl

if len(sys.argv) != 2:
    print('')
else:
    convert_dir = sys.argv[1]
    # 引数のディレクトリからテキストファイルを取得する
    text_paths = list(Path(convert_dir).glob('*.txt'))
    # 書き込み先のワークブックを作成する
    wb = openpyxl.Workbook()
    sheet = wb.active
    # 書き込み先列
    col_count = 1
    for path in text_paths:
        file = open(path)
        line_num = 1
        # 行ごとにワークブックに書き込む
        for line in file.readlines():
            sheet.cell(row=line_num, column=col_count).value = line
            line_num += 1
        col_count += 1
        file.close()

    wb.save('convertedExcel.xlsx')
    print('作成完了しました')
