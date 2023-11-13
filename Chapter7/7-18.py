import re


# 7.18.1 日付の検出
# DD/MM/YYYYの正規表現
def is_correct_date(date):
    date_regex = re.compile(r"""(
        (0[1-9]|[1-2][0-9]|3[0-1]) # 日付（00~31）
        /                          # 区切り
        (0[1-9]|1[0-2])            # 月(01~12)
        /                          # 区切り
        ([1-2][0-9]{3}$)           # 年(1000~2999)
        )""", re.VERBOSE)

    mo = date_regex.search(date)
    if mo is None:
        print(date + "は正しい日付ではありません")
        return

    # 正規表現で取得したDD/MM/YYYY形式の文字列を変数に代入
    day = int(mo.groups()[1])
    month = int(mo.groups()[2])
    year = int(mo.groups()[3])
    # 年がうるう年か判断する
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    is_correct_date = False

    # 日が正しい値かの判定
    if month == 2:
        # 2月の場合、うるう年なら29日、それ以外は28日までか
        if is_leap:
            is_correct_date = (day <= 29)
        else:
            is_correct_date = (day <= 28)
    # 4,6,9,11月の場合、30日までか
    elif month in [4, 6, 9, 11]:
        is_correct_date = (day <= 30)
    # それ以外の月の場合、31日までか
    else:
        is_correct_date = (day <= 31)

    if is_correct_date:
        print(date + "は正しい日付です")
    else:
        print(date + "は正しい日付ではありません")


# 7.18.2 強いパスワードの検出
def is_strong_password(password):
    # 8文字未満の場合
    if len(password) < 8:
        return False
    # 大文字を含まない場合
    elif re.compile(r'[A-Z]').search(password) is None:
        return False
    # 小文字を含まない場合
    elif re.compile(r'[a-z]').search(password) is None:
        return False
    # 数字を含まない場合
    elif re.compile(r'[0-9]').search(password) is None:
        return False
    return True


# 7.18.3 正規表現を用いたstrip()メソッド
def regex_strip(target, string=r'\s'):
    # 前方の除去
    strip_regex = re.compile(r'^(' + string + '*)')
    target = strip_regex.sub('', target)
    # 後方の除去
    strip_regex = re.compile(r'(' + string + '*)$')
    target = strip_regex.sub('', target)
    return target


# 7.18.1のテスト
is_correct_date('11/11/2031')
is_correct_date('11/11/3031')
is_correct_date('29/02/2000')
is_correct_date('29/02/1999')
is_correct_date('あいうえお')

# 7.18.2のテスト
print(is_strong_password('ABcd123'))
print(is_strong_password('AAAAbbbb'))
print(is_strong_password('0000AAAA'))
print(is_strong_password('0000vvvvv'))
print(is_strong_password('00aBcdEf'))

# 7.18.3のテスト
print(regex_strip('00abcd00', '0'))
print(regex_strip('  あああ ', ))
