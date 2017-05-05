#-*- coding:utf-8 -*-
#
# '''
# Addfriends 接口测试,测试账号:315325320@qq.com shanghai12
#
#     权限:
#         "email": "315325320@qq.com"
#         "authKey": "1c1a7edca9b44659b165cb9ad60c0bd2"
#         "X-ML-Session-Token": "dMer1pVSOTrsTqxBbrWLBBoyatCRxxHmvXRWhHr-l5k"
#         "X-ML-AppId": "57d6217122c9f6000137a4c2"
#
#     测试接口地址:
#         1.https://api.maxleap.com/2.0/functions/friendList
#         2.https://api.maxleap.com/2.0/functions/userInfo
#         3.https://api.maxleap.com/2.0/functions/friendInfo
#         4.https://api.maxleap.com/2.0/functions/updateFriend
#
# '''
#
# __author__="Wu jiajia"
#
#
# import requests
# import json
# import time
# import threading
# import sys,traceback
#
#
# class Thread(threading.Thread):
#     def __init__(self,target,args):
#         threading.Thread.__init__(self)
#         self.target = target
#         self.arges = args
#
#     def run(self):
#         self.target(self.arges)
#
#
# '''
#     Addfriends 接口测试,Addfriends类
# '''
#
#
# class Addfriends(object):
#     def __init__(self):
#         self.__privateVariable = 0
#     '''
#         装饰器log 打印接口测试日志
#     '''
#     def log(func):
#         def wrapper(*args,**kwargs):
#             try:
#                 runfc = func(*args,**kwargs)
#                 print '接口:',func.__name__,'测试通过'
#                 return runfc
#             except:
#                 print '接口:',func.__name__,'测试失败'
#                 traceback.print_exc()
#                 info = sys.exc_info()
#                 raise info[0], info[1]
#
#         return wrapper
#
#     @log
#     def get_friendslist(self,url):
#
#         headers = {
#             "Content-Type": "application/json",
#             "X-ML-Session-Token" : "dMer1pVSOTrsTqxBbrWLBBoyatCRxxHmvXRWhHr-l5k",
#             "X-ML-AppId" : "57d6217122c9f6000137a4c2",
#         }
#
#         currenttime = int(time.time())
#         postdata = {
#             "gender": 2,
#             "maxAge": 99,
#             "minAge": 13,
#             "age": 16,
#             "searchGender": 0,
#             "ver": "1.2",
#             "email": "15221685494@163.com",
#             "authKey": "48708cbe98ca4899991b6b590cc523ba",
#             "createdBefore":1478576632134
#         }
#
#         reponse = requests.post(url,headers=headers,data=json.dumps(postdata))
#         reponse.raise_for_status()
#
#         return json.loads(reponse.content)
#
#     @log
#     def get_userinfo(self,url):
#         headers = {
#             "Content-Type": "application/json",
#             "X-ML-Session-Token": "dMer1pVSOTrsTqxBbrWLBBoyatCRxxHmvXRWhHr-l5k",
#             "X-ML-AppId": "57d6217122c9f6000137a4c2",
#         }
#         postdata = {
#             "email": "2037704250@qq.com",
#             "authKey": "6cc4f27b1af24010ba5dcf651f9551ee",
#             "currentInstallationId": "3da315833e4343c58368f869f213789e"
#         }
#
#         reponse = requests.post(url, headers=headers, data=json.dumps(postdata))
#         reponse.raise_for_status()
#         return json.loads(reponse.content)
#
#     @log
#     def get_friendinfo(self,url):
#
#         headers = {
#             "Content-Type": "application/json",
#             "X-ML-Session-Token": "dMer1pVSOTrsTqxBbrWLBBoyatCRxxHmvXRWhHr-l5k",
#             "X-ML-AppId": "57d6217122c9f6000137a4c2",
#         }
#         postdata = {
#             "email": "2037704250@qq.com",
#             "authKey": "6cc4f27b1af24010ba5dcf651f9551ee"
#         }
#         reponse = requests.post(url, headers=headers, data=json.dumps(postdata))
#         reponse.raise_for_status()
#
#         return json.loads(reponse.content)
#
#     @log
#     def updatafriend(self,url,**postdata):
#
#         headers = {
#             "Content-Type": "application/json",
#             "X-ML-Session-Token": "dMer1pVSOTrsTqxBbrWLBBoyatCRxxHmvXRWhHr-l5k",
#             "X-ML-AppId": "57d6217122c9f6000137a4c2",
#         }
#         if not postdata :
#             default_postdata = {
#                 "gender": 1,
#                 "facebookUsername": "",
#                 "age": 18,
#                 "tags": ["fc53fe3e2ed44e25a57f40e9295f53d3"],
#                 "showToGender": 0,
#                 "bio": "",
#                 "instagramUsername": "lianjie1111",
#                 "vkUsername": "",
#                 "kikUsername": "kik",
#                 "friendName": "jiajiawu",
#                 "showToAgeMin": 17,
#                 "snapchatUsername": "",
#                 "authKey": "6cc4f27b1af24010ba5dcf651f9551ee",
#                 "email": "2037704250@qq.com",
#                 "interestedIn": 18,
#                 "showToAgeMax": 38
#             }
#
#             postdata = default_postdata
#
#
#         reponse = requests.post(url, headers=headers, data=json.dumps(postdata))
#         reponse.raise_for_status()
#
#         friendinfo = self.get_friendinfo('https://api.maxleap.com/2.0/functions/friendInfo')
#
#         del postdata['authKey']
#         del postdata["email"]
#
#         for key,value in postdata.items():
#             if value:
#                 v = friendinfo['friend'][0][key]
#                 if value != v:
#                     print key,value,'\n'
#                     print v
#                     raise Exception , u'更新失败!'
#
#         return json.loads(reponse.content)
#
#     def updata_me_info(self):
#
#         pass
#
# def runTest():
#
#     add = Addfriends()
#
#     threads = []
#     thread1 = Thread(add.get_friendslist,'https://api.maxleap.com/2.0/functions/friendList')
#     thread2 = Thread(add.get_userinfo,"https://api.maxleap.com/2.0/functions/userInfo",)
#     thread3 = Thread(add.get_friendinfo,"https://api.maxleap.com/2.0/functions/friendInfo")
#     thread4 = Thread(add.updatafriend,'https://api.maxleap.com/2.0/functions/updateFriend')
#
#     threads.append(thread1)
#     threads.append(thread2)
#     threads.append(thread3)
#     threads.append(thread4)
#
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#
# if __name__ == "__main__":
#     t1 = time.time()
#     runTest()
#     print '\n开始时间:',time.ctime(t1)
#     print '结束时间:',time.ctime(time.time())
#     print '运行时间:%ds'%int(time.time() - t1)
import datetime
import time

t = time.strptime('2016-09-28T08T:53:22.000Z',"%Y-%m-%dT%HT:%M:%SZ")
print t