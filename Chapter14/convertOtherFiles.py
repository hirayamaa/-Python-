import sys
import ezsheets

if len(sys.argv) != 2:
    print('引数の数が間違っています')
    print('python convertOtherFiles.py {ファイル名}')
else:
    ss = ezsheets.upload(sys.argv[1])
    print('アップロードが完了しました')
    file_name = 'converted_file'
    # エクセル、CSV、PDFに変換
    ss.downloadAsExcel(file_name + '.xlsx')
    ss.downloadAsCSV(file_name + '.csv')
    ss.downloadAsPDF(file_name + '.pdf')
    print('ダウンロードが完了しました')
