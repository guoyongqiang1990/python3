#-*- coding:utf-8 -*-
'''
Created on 2016年11月25日

@author: 杨立凯
'''
import os
import time
import HTMLTestRunner
import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from aw import *

rootPath = os.path.abspath(os.path.dirname(__file__))
# record = time.strftime("%Y-%m-%d_%H-%M-%S")
# spath = rootPath+"\\report\\"+"test_"+record
jsonFile="project.json"
    
def deviceList():
    devices=os.popen("adb devices").read()
    devices=devices.split("\n")
    deviceList=[]
    for line in devices:
        line=line.split("\t")
        if line[-1]=="device":
            deviceList.append(line[0])
        if line[-1]=="offline":
            print("%s is offline"%line[0])
#     print deviceList
    return deviceList 

def getOtaPackage(sn):
    git_release="\\\\10.8.0.22\software_release\git_release"
    _DATE=time.strftime("%Y-%m")
    product=DATA["auto_upgrade"]["product"]
    tag=DATA["auto_upgrade"]["tag"]
    phoneInfo=Common(sn).getGnVersion()
    if product not in phoneInfo:
        print("请确认手机型号与配置文件中是否一致")
    else:
        nowGnVersion=phoneInfo.split("_")[-1]
        print("手机当前版本为：" +nowGnVersion)
        #BJ_G1602A_sign_update_amigo3.5.0_T0121.zip
        rootdir=git_release+"\\"+_DATE+"\\02_ANDROID\\"+product
#         print rootdir
        for parent,dirnames,filenames in os.walk(rootdir): 
            for filename in  filenames:  
                if "ota" in parent and tag in parent and ".zip" in filename:
                    otapkg=filename.split("_")[-1] 
                    otapkg=otapkg.split(".")[0]
                    if otapkg > nowGnVersion:
                        print("待升级版本为：" +otapkg)
                        otapkgPath= parent+"\\"+filename
                    else:
                        otapkgPath=""
        print(otapkgPath)
        return otapkgPath

def autoOta(sn):   
    otaPackage=getOtaPackage(sn)
    zipFile=otaPackage.split("\\")[-1]
    try:
        if otaPackage:
            Common(sn).copyFile(otaPackage, "/storage/sdcard0/")
            Common(sn).unlockScreen()
            Common(sn).launchSettings()
            Common(sn).swipeToBottom()
            Common(sn).clickByText("系统升级")
            Common(sn).clickById("gn.com.android.update:id/menu_setting")
            Common(sn).clickByText("本地升级")
            Common(sn).clickByText("手动选择更新包")
            Common(sn).swipeToBottom()
            Common(sn).swipeToBottom()
            Common(sn).clickByText(zipFile)
            Common(sn).clickWhenExist(text="立即重启")
            time.sleep(1200)
            Common(sn).unlockScreen()
            Common(sn).clickWhenExist(text="立即体验")
            print("OTA升级完成")
            Common(sn).reboot()
            Common(sn).unlockScreen()
            return True
        else:
            print("当前已是最新版本")
            return False
    except Exception as e:
        print(e)
        return False
    
def otaThreads():
    threadsList=[]
    for sn in deviceList():
        t = threading.Thread(target=autoOta,args=(sn) )
        threadsList.append(t)
#     print threadsList
    for t in threadsList:
        t.setDaemon(True)
        t.start()
        time.sleep(5)
    for t in threadsList:
        t.join()

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
    s=s.replace(A, B)
    f.close()
    p=open(rootPath+"\\"+jsonFile,"w+")
    p.write(s)
    p.close()

def sendEmail(newfile):
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

def toRun(cfgFileName="project"):
    spath = rootPath+"\\report\\"+"test_"+time.strftime("%Y-%m-%d_%H-%M-%S")
    changeConfig("\"screencap\":\"no\"", "\"screencap\":\"yes\"")
    f = open(rootPath+"\\project.log", 'w+') 
    f.write(spath)
    f.close()
#     print >>f,spath
    os.makedirs(spath)
    print ("Report saved to :"+spath)
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
   
if __name__=="__main__": 
#     Common(DUT).uninstallApp("com.github.uiautomator")
#     Common(DUT).uninstallApp("com.github.uiautomator.test")
    waitTime=3*3600
    Common(DUT).unlockScreen()
    if len(deviceList()):
        while DATA["auto_upgrade"]["OTA"]=="yes":
            if DATA["auto_upgrade"]["next"]=="yes":
                newfile=toRun()
                sendEmail(newfile)
                while not autoOta(DUT):
                    print("未升级新版本,等待 "+str(waitTime/3600)+"小时后继续 ")
                    time.sleep(waitTime)
                    continue
                else:
                    continue
    
            elif DATA["auto_upgrade"]["next"]=="no":
                while not autoOta(DUT):
                    print("未升级新版本,等待 "+str(waitTime/3600)+"小时后继续")
                    time.sleep(waitTime)
                    continue
                else:
                    newfile=toRun()
                    sendEmail(newfile)
                    continue
        else:
            newfile=toRun()
            sendEmail(newfile)
    else:
        print("请检查设备连接状态")

            
    