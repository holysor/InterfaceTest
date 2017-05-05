# -*- coding:UTF-8 -*-
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #导入附件模块
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import pandas
import codecs
import os

''''收件人'''
mailto_list = ["15221685494@sina.cn"]

'''设置服务器，用户名、口令以及邮箱的后缀'''
#==========================================
mail_host = "smtp.163.com"
mail_user = "15221685494"
mail_pass = "holysor520"
mail_postfix = "163.com"

#==========================================
'''发送邮件'''
def send_mail(to_list, sub):
    '''''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("xxx@xxx.com","sub","content")
    '''
    # print os.getcwd()
    xd = pandas.ExcelFile(os.getcwd()+os.sep+'Report/Report.xlsx')
    df = xd.parse(xd.sheet_names[1], header=None, keep_default_na=False)


    html_head = u"""<html><head><title>接口测试报告</title></head><body>
        <p>接口测试报告,附件查看报告细节</p>"""

    html =html_head + df.to_html(header=False, index=False)

    # print html
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEMultipart('alternative')
    #   msg["Accept-Language"]="zh-CN"
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ",".join(to_list)

    #邮件内容
    msg.attach(MIMEText(html,'html',_charset='utf-8'))


    #构造邮件附件
    part = MIMEApplication(open(os.getcwd()+os.sep+'Report/Report.xlsx','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="Report.xlsx")
    msg.attach(part)

    day = time.strftime('%Y-%m-%d')
    filename = os.getcwd()+os.sep+ 'Report/report'+day+'.html'
    att = MIMEText(open(filename,'rb').read(),"base64",'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="Report.html"'
    msg.attach(att)

    try:
        server = smtplib.SMTP()
        #账户加密
        # server.starttls()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.set_debuglevel(1)
        server.quit()
        return True
    except Exception, e:
        print str(e)
        return False

def testEmail():
    print '发送邮件'
    subject = u'Fluk接口测试报告'
    if send_mail(mailto_list, subject):
        print "\n发送成功"
    else:
        print "\n发送失败"

if __name__ == '__main__':
    testEmail()