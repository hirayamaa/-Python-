import ezsheets

ss = ezsheets.createSpreadsheet('My SpreadSheet')
sheet = ss[0]
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['C1'] = 'Favorite Movie'

# B1を表示
print(sheet[2, 1])
sheet['A2'] = 'Alice'
sheet['B2'] = '30'
sheet['C2'] = 'RoboCop'

