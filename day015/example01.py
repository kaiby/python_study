"""
example - 操作Excel

三方库:
    xlrd xlwt xlutils 低版本
    openpyxl 高版本

Author: kaiby
Date: 2024/1/12 13:43
"""
import xlrd

wb = xlrd.open_workbook('id.xls')
print(wb.sheet_names())
# sheet = wb.sheet_by_name('tem4')
sheet = wb.sheet_by_index(0)
print(type(sheet))
print(sheet.name, sheet.nrows, sheet.ncols)
# print(sheet.row(0))
# print(sheet.row_slice(1, 0, 5))
# print(sheet.col(4))
# print(sheet.col_slice(1, 5, 10))
# cell = sheet.cell(7, 1)
# print(cell.value)

for row in range(1, sheet.nrows):
    for col in range(sheet.ncols):
        cell = sheet.cell(row, col)
        if col == 0:
            print(f'{int(cell.value):>2d}', end=' ')
        if col == 8:
            year, month, day, *_ = xlrd.xldate_as_tuple(cell.value, 0)
            # date = xlrd.xldate_as_datetime(cell.value, 0)
            # print(date.strftime('%Y年%m月%d日'), end=' ')
            print(f'{year}年{month}月{day}日', end=' ')
        else:
            print(cell.value, end=' ')
    print()
