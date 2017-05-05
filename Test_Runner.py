#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,sys
import traceback
import time
import unittest

import configparser
import xlrd
from xlutils.copy import copy

from Public.Basehttp import BaseHttp
from Public import HTMLTestRunner
from Public.confighttp import *
from Public.Excelreport import *
from Public.Sendemail import *
# 定义结构体
class DataStruct:
    '''于接收 excel 读取的测试数据,记录要写入测试报告的数据'''

    pass

test_data = DataStruct()
test_data.url = ''                          # 接收接口 url
test_data.params = {}                       # 接收接口参数
test_data.expected_result = {}              # 接收预期结果
test_data.result = {}                   # 接收测试结果
test_data.exceldata = {
    "info":[],
    "test_sum": 0,
    "test_success":0,
    "test_failed":0,
}


# 测试用例(组)类
class TestInterfaceCase(unittest.TestCase):
    # 测试用例(组)类
    def setUp(self):
        base_http = BaseHttp('Public/conf.ini')
        self.config_http = ConfigHttp(base_http.get_host())

    # 测试接口1
    def test_updatafriend(self):
        # 根据被测接口的实际情况，合理的添加 HTTP 头
        header = {
            "Content-Type": "application/json",
            "X-ML-Session-Token": "dMer1pVSOTrsTqxBbrWLBBoyatCRxxHmvXRWhHr-l5k",
            "X-ML-AppId": "57d6217122c9f6000137a4c2",
        }
        self.config_http.set_header(header)
        response = self.config_http.post(test_data.url, test_data.params)
        if response == {}:
            test_data.result[2] = 'error'
            set_result(2,'Error')
            raise Exception,'Return JSON data is empty'

        try:
            self.assertEqual(response['code'], int(test_data.expected_result[2]),'exception')
            test_data.result[2] = 'Pass'
        except AssertionError,e:
            test_data.result[2] = 'Fail'
            raise AssertionError,e.message

        finally:
            set_result(2, test_data.result[2])
    # 测试接口2
    def test_get_friendslist(self):
        header = {
            "Content-Type": "application/json",
            "X-ML-Session-Token": "dMer1pVSOTrsTqxBbrWLBBoyatCRxxHmvXRWhHr-l5k",
            "X-ML-AppId": "57d6217122c9f6000137a4c2",
        }
        self.config_http.set_header(header)
        response = self.config_http.post(test_data.url, test_data.params)
        if {} == response:
            test_data.result[1] = 'Error'
            set_result(1, 'Error')
            raise Exception,'Return JSON data is empty'

        try:
            self.assertEqual(response['code'], int(test_data.expected_result[1]),msg='Return error')
            test_data.result[1] = 'Pass'
        except AssertionError,e:

            test_data.result[1] = 'Fail'
            raise AssertionError,e.message
        finally:
             set_result(1, test_data.result[1])


    def tearDown(self):
        pass

def set_result(id,rs):
    for n in range(len(test_data.exceldata['info'])):
        if int(test_data.exceldata['info'][n]['t_id']) == id:
            test_data.exceldata['info'][n]['t_result'] = rs

# 获取测试套件
def get_test_suite(index):
    function = sheet1.row_values(index)[8]  # 根据选择的用例，获取对应的测试用例方 法
    testsuite.addTest(TestInterfaceCase(function))

# 运行测试用例函数
def run_case(sheet, runner, config_file=''):
    config = configparser.ConfigParser()
    # 从配置文件中读取要运行测试的测试用例所在行索引
    config.read(config_file)
    try:
        run_mode = config['DEFAULT']['runmode']
        run_mode = int(run_mode)  # 把字符串类型的转换为 list

    except Exception:
        print('error happend in case config_file')

    if run_mode == True: # 运行全部用例
        # 获取用例个数
        test_case_num = sheet.nrows

        for index in range(1, test_case_num):
            test_data.url = sheet.row_values(index)[4]
            test_data.params = json.loads(sheet.row_values(index)[5])
            test_data.expected_result[sheet.row_values(index)[0]] = sheet.row_values(index)[6]
            test_hope = sheet.row_values(index)[6]
            test_data.result[sheet.row_values(index)[0]] = ''
            caseid = sheet.row_values(index)[0]
            name = sheet.row_values(index)[1]
            method = sheet.row_values(index)[2]
            infodata = {
                "t_id": caseid,
                "t_name": name,
                "t_method": method,
                "t_url": test_data.url,
                "t_param": test_data.params,
                "t_hope": test_hope,
                "t_actual": '',
                "t_result": ''
            }
            test_data.exceldata["info"].append(infodata)
            get_test_suite(index)

    else:
        try:
            case_list = config['DEFAULT']['index']
            case_list = eval(case_list)  # 把字符串类型的 list 转换为 list
        except Exception:
            print('error happend in case config_file')

        for index in case_list:
            test_data.url = sheet.row_values(index)[4]
            test_data.params = json.loads(sheet.row_values(index)[5])
            test_data.expected_result[sheet.row_values(index)[0]] = sheet.row_values(index)[6]
            test_data.result[sheet.row_values(index)[0]] = ''
            test_hope = sheet.row_values(index)[6]

            caseid = sheet.row_values(index)[0]
            name = sheet.row_values(index)[1]
            method = sheet.row_values(index)[2]
            infodata = {
                "t_id": caseid,
                "t_name": name,
                "t_method": method,
                "t_url": test_data.url,
                "t_param": test_data.params,
                "t_hope": test_hope,
                "t_actual": '',
                "t_result": ''
            }
            test_data.exceldata["info"].append(infodata)
            # print test_data.exceldata
            get_test_suite(index)


if __name__=='__main__':
    # 记录测试开始时间
    start_time = time.time()
    now = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d')
    htmlpath =  os.getcwd() + os.sep + 'Report' + os.sep + 'report' + day + '.html'
    file_is_exist = os.path.exists(htmlpath)
    if file_is_exist:
        os.remove(htmlpath)
    fp = file(htmlpath,'wb')

    # runner = unittest.TextTestRunner(verbosity=2)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化接口测试报告', description=u'进行Fluk接口测试,验证接口返回参数')
    testsuite = unittest.TestSuite()

    #  读取用例数据

    excel = xlrd.open_workbook('Public/TestCase.xls',formatting_info=True)
    sheet1 = excel.sheet_by_index(0)
    run_case(sheet1, runner, 'Public/case_config.ini')

    test_result= runner.run(testsuite)


    # print test_result.failures, test_result.errors, test_result.testsRun

    data = {"test_sum": test_result.testsRun, "test_success": test_result.success_count, "test_failed": test_result.failure_count+test_result.error_count, "test_date": now}

    init(worksheet,data)
    test_detail(worksheet2,test_data.exceldata)
    workbook.close()
    testEmail()
