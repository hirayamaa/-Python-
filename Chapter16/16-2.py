import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# csvディレクトリ内の全ファイルをループする
for csv_filename in os.listdir('csvFile'):
    if not csv_filename.endswith('.csv'):
        continue
    print(f'見出し削除中 {csv_filename}...')
    # csvファイルを読み込む(最初の行をスキップする)
    csv_rows = []
    csv_file_obj = open(os.path.join('csvFile', csv_filename))
    reader_obj = csv.reader(csv_file_obj)
    # csvファイルを読み込む
    for row in reader_obj:
        # 最初の行をスキップする
        if reader_obj.line_num == 1:
            continue
        csv_rows.append(row)
    csv_file_obj.close()
    # csvファイルを書き出す
    csv_file_obj = open(os.path.join('headerRemoved', csv_filename), 'w', newline='')
    csv_writer = csv.writer(csv_file_obj)
    for row in csv_rows:
        csv_writer.writerow(row)
    csv_file_obj.close()
