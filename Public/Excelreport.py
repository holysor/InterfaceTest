# -*- coding: utf-8 -*-
import xlsxwriter

def get_format(wd, option={}):
    return wd.add_format(option)

# 设置居中
def get_format_center(wd,num=1):
    return wd.add_format({'align': 'center','valign': 'vcenter','border':num})
def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)

# 写数据
def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))

PATH = 'Report/Report.xlsx'
workbook = xlsxwriter.Workbook(PATH)
worksheet = workbook.add_worksheet(u"测试总况")
worksheet2 = workbook.add_worksheet(u"测试详情")


def init(worksheet,Rdata):

    # 设置列行的宽高
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)

    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)

    # worksheet.set_row(0, 200)

    define_format_H1 = get_format(workbook, {'bold': True, 'font_size': 18})
    define_format_H2 = get_format(workbook, {'bold': True, 'font_size': 14})
    define_format_H1.set_border(1)

    define_format_H2.set_border(1)
    define_format_H1.set_align("center")
    define_format_H2.set_align("center")
    define_format_H2.set_bg_color("blue")
    define_format_H2.set_color("#ffffff")
    # Create a new Chart object.

    worksheet.merge_range('A1:F1', u'测试报告总概况', define_format_H1)
    worksheet.merge_range('A2:F2', u'测试概括', define_format_H2)
    worksheet.merge_range('A3:A6', u'添加图片', get_format_center(workbook))

    _write_center(worksheet, "B3", u'项目名称', workbook)
    _write_center(worksheet, "B4", u'接口版本', workbook)
    _write_center(worksheet, "B5", u'测试设备', workbook)
    _write_center(worksheet, "B6", u'测试网络', workbook)


    data = {"test_name": u"Fluk", "test_version": "v2.4", "test_pl": "IOS", "test_net": "wifi"}

    _write_center(worksheet, "C3", data['test_name'], workbook)
    _write_center(worksheet, "C4", data['test_version'], workbook)
    _write_center(worksheet, "C5", data['test_pl'], workbook)
    _write_center(worksheet, "C6", data['test_net'], workbook)

    _write_center(worksheet, "D3", u"接口总数", workbook)
    _write_center(worksheet, "D4", u"通过总数", workbook)
    _write_center(worksheet, "D5", u"失败总数", workbook)
    _write_center(worksheet, "D6", u"测试日期", workbook)



    # data1 = {"test_sum": 100, "test_success": 80, "test_failed": 20, "test_date": "2018-10-10 12:10"}

    data1 = Rdata
    _write_center(worksheet, "E3", data1['test_sum'], workbook)
    _write_center(worksheet, "E4", data1['test_success'], workbook)
    _write_center(worksheet, "E5", data1['test_failed'], workbook)
    _write_center(worksheet, "E6", data1['test_date'], workbook)

    _write_center(worksheet, "F3", u"分数", workbook)


    worksheet.merge_range('F4:F6', '60', get_format_center(workbook))

    pie(workbook, worksheet)

 # 生成饼形图
def pie(workbook, worksheet):
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
    'name':u'接口测试统计',
    'categories':u'=测试总况!$D$4:$D$5',
   'values':    u'=测试总况!$E$4:$E$5',
    })
    chart1.set_title({'name': u'接口测试统计'})
    chart1.set_style(10)
    worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})

def test_detail(worksheet,data):

    # 设置列行的宽高
    worksheet.set_column("A:A", 30)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)
    worksheet.set_column("G:G", 20)
    worksheet.set_column("H:H", 20)

    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)
    worksheet.set_row(6, 30)
    worksheet.set_row(7, 30)



    worksheet.merge_range('A1:H1', u'测试详情', get_format(workbook, {'bold': True, 'font_size': 18 ,'align': 'center','valign': 'vcenter','bg_color': 'blue', 'font_color': '#ffffff'}))
    _write_center(worksheet, "A2", u'用例ID', workbook)
    _write_center(worksheet, "B2", u'接口名称', workbook)
    _write_center(worksheet, "C2", u'接口协议', workbook)
    _write_center(worksheet, "D2", u'URL', workbook)
    _write_center(worksheet, "E2", u'参数', workbook)
    _write_center(worksheet, "F2", u'预期值', workbook)
    _write_center(worksheet, "G2", u'实际值', workbook)
    _write_center(worksheet, "H2", u'测试结果', workbook)

    temp = 3
    for item in data["info"]:
        _write_center(worksheet, "A"+str(temp), item["t_id"], workbook)
        _write_center(worksheet, "B"+str(temp), item["t_name"], workbook)
        _write_center(worksheet, "C"+str(temp), item["t_method"], workbook)
        _write_center(worksheet, "D"+str(temp), item["t_url"], workbook)
        _write_center(worksheet, "E"+str(temp), str(item["t_param"]), workbook)
        _write_center(worksheet, "F"+str(temp), str(item["t_hope"]), workbook)
        _write_center(worksheet, "G"+str(temp), str(item["t_actual"]), workbook)
        _write_center(worksheet, "H"+str(temp), item["t_result"], workbook)
        temp += 1
        if temp >len(data['info'])+2:
            break

if __name__ == '__main__':
    # init(worksheet,)
    test_detail(worksheet2)

    workbook.close()