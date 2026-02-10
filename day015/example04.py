"""
example04 - 

Author: kaiby
Date: 2024/1/15 14:04
"""
import random

import xlwt

# 创建工作簿
wb = xlwt.Workbook()

# 创建工作表
sheet = wb.add_sheet('成绩')  # type:xlwt.Worksheet

# 向单元格写入数据

# 创建样式
header_style = xlwt.XFStyle()
header_pattern = xlwt.Pattern()
header_pattern.pattern = xlwt.Pattern.SOLID_PATTERN
header_pattern.pattern_fore_colour = xlwt.Style.colour_map['aqua']
header_style.pattern = header_pattern
header_font = xlwt.Font()
header_font.height = 20 * 22
header_font.bold = True
header_style.font = header_font
# 对齐
header_alignment = xlwt.Alignment()
# 垂直对齐
header_alignment.vert = xlwt.Alignment.VERT_CENTER
# 水平对齐
header_alignment.horz = xlwt.Alignment.HORZ_CENTER
header_style.alignment = header_alignment

sheet.write(0, 0, '姓名', header_style)
sheet.write(0, 1, '语文', header_style)
sheet.write(0, 2, '数学', header_style)
sheet.write(0, 3, '英语', header_style)

students = ('Tom', 'Jerry', 'Anna', 'Emma', 'Junior')

for i in range(len(students)):
    sheet.write(i + 1, 0, students[i])
    for col in range(1, 4):
        sheet.write(i + 1, col, random.randrange(40, 101))

# 保存
wb.save('score.xls')
