#-*- coding:utf-8 -*-
'''
Created on 2016年11月25日

@author: 杨立凯
'''
import os
import time
import json
import unittest
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

rootPath = os.path.abspath(os.path.dirname(__file__))
record = time.strftime("%Y-%m-%d_%H-%M-%S")
spath = rootPath+"\\report\\"+"test_"+record
jsonFile="project.json"

def getModuleList():
    moduleList=[]
    with open(rootPath+"\\test.txt") as f:
        for line in f.readlines():
            line=line.split()[0]
            line=line.split(".")[0]
            if line[0] !="#" and len(line) != 0:
                moduleList.append(line)
    print("计划执行用例 :"+str(len(moduleList))+"条")
    return moduleList 
     
def testSuit():
    suite = unittest.TestSuite()
    for m in getModuleList():
        if "\\" in m:
            m=m.replace("\\",".")      
            testModule = __import__(m,{},{},["test"])
        else:
            testModule = __import__("test.PowerConsumption."+m,{},{},["test"])
        suite.addTest(testModule.TestScript('test_step'))
    return suite 

def changeConfig(A, B):
    f= open(rootPath+"\\"+jsonFile,"r")
    s=f.read()
#     s=s.replace("\"screencap\":\"no\"","\"screencap\":\"yes\"")
    s=s.replace(A, B)
    f.close()
    p=open(jsonFile,"w+")
    p.write(s)
    p.close()
#     print s

def toRun(cfgFileName="project"):
    changeConfig("\"screencap\":\"no\"", "\"screencap\":\"yes\"")
    with open(rootPath+"\\project.log", 'w+') as f: 
        f.write(spath)
#     print >>f,spath
    os.makedirs(spath)
    print ("Report saved to :"+spath)
#     filename = spath+"\\Test_Report_"+record+".html"
    filename = spath+"\\Test_Report.html"
    fp = open(filename,'wb')
    print(cfgFileName+" is running")
#     runner = unittest.TextTestRunner()
#     runner.run(testSuit())
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="AutoTestReport",description='Power Consumption')
    runner.run(testSuit())
    fp.close()
    changeConfig("\"screencap\":\"yes\"", "\"screencap\":\"no\"")
    return filename

def sendEmail(newfile):
    jsonFile="project.json"
    with open(rootPath+"\\"+jsonFile,"r") as f:
        DATA = json.load(f) 
    if DATA["send_email"]["send"]=="yes":
        #打开文件
        f=open(newfile,'rb')
        #读取文件内容
        mail_body=f.read()
    #     print mail_body
        f.close()
        #发送邮箱服务器
        smtpserver = DATA["send_email"]["smtpserver"]
        #发送邮箱用户名/密码
        user=DATA["send_email"]["user"]
        password=DATA["send_email"]["password"]
        #发送邮箱
        sender=DATA["send_email"]["sender"]
        #多个接收邮箱
        receiver=DATA["send_email"]["receiver"]
        #发送邮件主题
        subject = '【自动化功耗测试】G1602A T0096版本功耗测试报告（自动发送）'
        msg=MIMEMultipart('mixed')          
    #    msg_plain = MIMEText(text,'plain', 'utf-8')    
    #    msg.attach(msg_plain)         
        msg_html1 = MIMEText(mail_body,'html','utf-8')
        msg.attach(msg_html1)
        msg_html = MIMEText(mail_body,'html','utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)    
#         msg['From'] = 'yanglk@gionee.com <yanglk@gionee.com>'
        msg['To'] = ";".join(receiver)
        msg['Subject']=Header(subject,'utf-8')     
        #连接发送邮件
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver,25)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    else:
        pass  
    
if __name__=="__main__": 
    newfile=toRun()
    sendEmail(newfile)
    