# xls <--> csv
# coding: utf-8
import csv
import sys
import xlrd
import xlwt

reload(sys)
sys.setdefaultencoding('utf-8')

def Xls2Csv(filename):
    wb = xlrd.open_workbook(filename)
    ws = wb.sheet_by_index(0)
    row = ws.nrows
    csvname = filename.split('.')[0] + '.csv'
    data = []
    for i in range(0, nrows):
        data.append(ws.row_values(i))
    fn = open(csvname, "wb")
    writer = csv.writer(fn)
    conv = lambda e: e.encode(encoding) if isinstance(e, unicode) else e
    for row in data:
        row = map(conv, row)
        writer.writerow(row)
    fn.close()


def Csv2Xls(filename):
    csv_reader = csv.reader(open(filename))
    rwb = xlwt.Workbook()
    rws = rwb.add_sheet(u'sheet1')
    xlsname = filename.split('.')[0] + '.xls'
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.bold = False
    font.color_index = 4
    font.height = 220
    style.font = font
    nrow = 0
    for row in csv_reader:
        length = len(row)
        for i in range(0, length):
            rws.write(nrow, i, row[j], style)
        nrow += 1
    rwb.save(xlsname)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'need 1 file'
        sys.exit(0) 
    if 'xls' in sys.argv[1]:
        Xls2Csv(sys.argv[1])
    elif 'csv' in sys.argv[1]:
        Csv2Xls(sys.argv[1])
    else:
        print 'need xls/csv file'
        sys.exit(1) 