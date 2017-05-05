# -*- coding:UTF-8 -*-
import pandas
import codecs
import chardet
import xlrd
xd = pandas.ExcelFile('../Report/Report.xlsx')
df = xd.parse(xd.sheet_names[1],header=None, keep_default_na=True)


with codecs.open("report.html", "w","gb2312") as html_fil:
    html_fil.write(df.to_html(header=False, index=False,))



# f = open('../Report/Report.xlsx','rb')
# print chardet.detect(f.read())

workbook  = xlrd.open_workbook('../Report/Report.xlsx')

sheet = workbook.sheet_by_index(1)

print sheet._cell_values