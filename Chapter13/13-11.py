import openpyxl.chart

wb = openpyxl.Workbook()
sheet = wb.active
# A列に適当なデータを作成する
for i in range(1, 11):
    sheet[f'A{i}'] = i
# Referenceオブジェクトを作成する（データが入力されているセルを指定する。下記ではA1:A10を指定している）
ref_obj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1,
                                   max_col=1, max_row=10)
# Referenceオブジェクトを渡してSeriesオブジェクトを作成する
series_obj = openpyxl.chart.Series(ref_obj, title='First series')
# Chartオブジェクトを作成する
chart_obj = openpyxl.chart.BarChart()
chart_obj.title = 'My Chart'
# ChartオブジェクトにSeriesオブジェクトを追加する
chart_obj.append(series_obj)
# シートにChartオブジェクトを追加
sheet.add_chart(chart_obj, 'C5')
wb.save('sampleChart.xlsx')
