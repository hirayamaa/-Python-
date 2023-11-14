import pyinputplus as pyip

prices = {
    '小麦パン': 200,
    '白パン': 250,
    'サワー種': 300,
    'チキン': 100,
    'ターキー': 150,
    'ハム': 80,
    '豆腐': 60,
    'チェダー': 25,
    'スイス': 27,
    'モッツァレラ': 28,
    'マヨネーズ': 22,
    'からし': 24,
    'レタス': 25,
    'トマト': 21,
}
# サンドイッチ１個の合計金額
sum_price = 0

response = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'],
                          prompt='パンを選んでください\n', numbered=True)
sum_price += prices[response]
print(response + f'は{prices[response]}円になります')

response = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'],
                          prompt='タンパク質を選んでください\n', numbered=True)
sum_price += prices[response]
print(response + f'は{prices[response]}円になります')

need_cheese = pyip.inputYesNo('チーズは必要ですか？')
if need_cheese == 'yes':
    response = pyip.inputMenu(['チェダー', 'スイス', 'モッツァレラ'],
                              prompt='チーズを選んでください\n', numbered=True)
    sum_price += prices[response]
    print(response + f'は{prices[response]}円になります')

if pyip.inputYesNo('マヨネーズは必要ですか？') == 'yes':
    sum_price += prices['マヨネーズ']
    print(f'マヨネーズは{prices['マヨネーズ']}円になります')

if pyip.inputYesNo('からしは必要ですか？') == 'yes':
    sum_price += prices['からし']
    print(f'からしは{prices['からし']}円になります')

if pyip.inputYesNo('レタスは必要ですか？') == 'yes':
    sum_price += prices['レタス']
    print(f'レタスは{prices['レタス']}円になります')

if pyip.inputYesNo('トマトは必要ですか？') == 'yes':
    sum_price += prices['トマト']
    print(f'トマトは{prices['トマト']}円になります')

sandwich_num = pyip.inputInt('サンドイッチが幾つ必要ですか？', min=1)
print(f'合計金額は{sum_price * sandwich_num}円です')
