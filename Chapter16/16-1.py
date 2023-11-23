import csv

example_file = open('csvFile/example.csv')
# readerオブジェクトを作成
example_reader = csv.reader(example_file)

# forループでCSVの値を読み出す(ループは1回のみ）
for row in example_reader:
    print(f'Row #{example_reader.line_num} {row}')
example_file.close()
print('########################################')

# CSVファイルに書き込む
output_file = open('csvFile/output.csv', 'w', newline='')
output_write = csv.writer(output_file)
output_write.writerow(['span', 'eggs', 'bacon', 'ham'])
output_write.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
output_write.writerow([1, 2, 3.141592, 4])
output_file.close()


tsv_file = open('csvFile/example.tsv', 'w', newline='')
# セル間をタブ文字に、行間を2つの改行文字にする（1行ごとに1行あく）
tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n\n')
tsv_writer.writerow(['apples', 'oranges', 'grapes'])
tsv_writer.writerow(['eggs', 'bacon', 'ham'])
tsv_writer.writerow(['spam', 'spam', 'spam', 'spam', 'spam'])
tsv_file.close()

# withHeaderファイルの作成
csv_file = open('csvFile/example.csv')
csv_reader = csv.reader(csv_file)
with_header_file = open('csvFile/exampleWithHeader.csv', 'w', newline='')
csv_writer = csv.writer(with_header_file)
csv_writer.writerow(['Timestamp', 'Fruit', 'Quantity'])
for row in csv_reader:
    csv_writer.writerow(row)
csv_file.close()
with_header_file.close()

# DictReaderとDictWriterオブジェクト
example_file = open('csvFile/exampleWithHeader.csv')
example_dict_reader = csv.DictReader(example_file)
for row in example_dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
example_file.close()
print('########################################')

# ヘッダー行のないCSVの場合
example_file = open('csvFile/example.csv')
# 第2引数で列名のリストを渡すことでヘッダーありのCSVとして扱える
example_dict_reader = csv.DictReader(example_file, ['time', 'name', 'amount'])
for row in example_dict_reader:
    print(row['time'], row['name'], row['amount'])
example_file.close()
print('########################################')

output_file = open('csvFile/output.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
# ヘッダー行をCSVファイルに書き込む
output_dict_writer.writeheader()
# 辞書形式で書き込むことができる
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
output_file.close()
