import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']
# フォントを作成
italic_24_font = Font(size=24, italic=True)
sheet['A1'].font = italic_24_font
sheet['A1'] = 'Hello World!'
wb.save('styles.xlsx')

# 13-8 Fontオブジェクト
font_obj1 = Font(name='Times New Roman', bold=True)
sheet['A2'].font = font_obj1
sheet['A2'] = 'Bold Times New Roman'
wb.save('styles.xlsx')

# 13-9 数式
sheet['D1'] = 200
sheet['D2'] = 300
sheet['D3'] = 400
# 数式を設定
sheet['D4'] = '=SUM(D1:D3)'
wb.save('styles.xlsx')

