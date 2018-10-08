#-*- coding:utf-8 -*-
'''
Created on 2016.11.25

@author: 杨立凯
'''
import time,datetime
import os,sys
import json
import threading
from logger import Logger
import subprocess
from uiautomator import Device

rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
def config():
    jsonFile="project.json"
    with open(rootPath+"\\"+jsonFile,"r") as f:
        config = json.load(f)
    return config

def step(func):
    def wraper(*args,**kwargs):
        func(*args,**kwargs)
        time.sleep(0.5)
        _screenShot()
    return wraper

def _screenShot():
    with open(rootPath+"\\project.log","r") as f:
        savePath = f.readline().strip()
    if config()["log_config"]["screencap"]=="yes":
        record = time.strftime("%Y-%m-%d_%H-%M-%S")
        imagepath="/data/local/tmp/"+record+".png"
        sn=config()["device"]["DUT"]["sn"]
        if sn =="None":
            subprocess.Popen("adb shell screencap -p "+imagepath, shell=True).wait()
            subprocess.Popen("adb pull "+imagepath+" " + savePath+"\\"+record+".png", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            print("<a href=\""+savePath+"\\"+record+".png\""+ " target=\"_blank\">点击查看截图</a>")
            subprocess.Popen("adb shell rm "+imagepath).wait()
        else:
            subprocess.Popen("adb -s %s shell screencap -p "%sn+imagepath, shell=True).wait()
            subprocess.Popen("adb -s %s pull "%sn+imagepath +" "+ savePath+"\\"+record+".png", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            print("<a href=\""+savePath+"\\"+record+".png\""+ " target=\"_blank\">点击查看截图</a>")
            subprocess.Popen("adb -s %s shell rm "%sn+imagepath, shell=True).wait()
        
class Common(object):
    def __init__(self,sn=None):
        global d
        d=Device(sn)
        self.sn=sn
#         self.rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
#         f = open(self.rootPath+"\\project.log","r")
#         self.savePath = f.readline().strip()
        self.record = time.strftime("%Y-%m-%d_%H-%M-%S")
       
    def screenShot(self):
        with open(rootPath+"\\project.log","r") as f:
            savePath = f.readline().strip()
        imagepath="/data/local/tmp/"+self.record+".png"
        if self.sn ==None:
            os.popen("adb shell screencap -p "+imagepath)
            os.popen("adb pull "+imagepath+" " + savePath+"\\"+self.record+".png")
#             Logger.info("截图保存至："+self.savePath+"\\"+self.record+".png")
            os.popen("adb shell rm "+imagepath)
        else:
            os.popen("adb -s %s shell screencap -p "%self.sn+imagepath)
            os.popen("adb -s %s pull "%self.sn+imagepath +" "+ savePath+"\\"+self.record+".png")
            os.popen("adb -s %s shell rm "%self.sn+imagepath)
#         return self.savePath+"\\"+self.record+".png"   
        
    def shell(self,cmd):
        return self.adbCmd("shell "+cmd)
            
    def adbCmd(self,cmd):
        if self.sn==None:
#             os.system("adb "+cmd)
            subprocess.Popen("adb "+cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
#             print ret
            Logger.info("adb "+cmd)
        else:
#             os.system("adb -s %s "%self.sn+cmd)
            subprocess.Popen("adb -s %s "%self.sn+cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
#             print ret
            Logger.info("adb -s %s "%self.sn+cmd)
#         return ret
            
    def wait(self,seconds):
        time.sleep(seconds)
    
    @step
    def startActivity(self,activity_name,timeOut=2):
        self.shell("am start -n "+activity_name)
        time.sleep(timeOut)
        self.clickWhenExist(text="继续")
    
    @step   
    def click(self,x,y):
        '''
        1. 点击绝对坐标
        '''
        d.click(x, y)
        self.wait(1)
        
    @step     
    def clickObject(self, **keyargs):
        d(**keyargs).click()
        
    def click_relative(self, a, b, waitTime=1):
        '''
        1. 点击相对坐标
        '''
        x, y=self.getScreenSize()
        self.click(a*x, b*y)
        self.wait(waitTime)
        
    @step 
    def long_click(self,x,y):
        '''
        1. 长点击
        '''
        d.long_click(x, y) 
        
    @step      
    def clickByText(self,text,index=0,screeScroll=False,direction="up_down",timeout=20,waitTime=0.5):
        if screeScroll==True:
            startTime=time.time()
            while time.time()-startTime<timeout :
                if d(text=text, instance=index).exists:
                    d(text=text,instance=index).click()
                    Logger.info("click text: "+text)
                    time.sleep(0.1)
                    break
                else:
                    if direction=="up_down":
                        d.swipe(500, 800, 500, 200, 40)
                    if direction=="left_right":
                        d.swipe(700, 500, 100, 500, 40)
                    time.sleep(waitTime)
        else:
            d(text=text,instance=index).click()
            Logger.info("click text: "+text)
            self.wait(1)
    @step         
    def long_clickByText(self,text,index=0,screeScroll=False,direction="up_down",timeout=20,waitTime=2):
        if screeScroll==True:
            startTime=time.time()
            while time.time()-startTime<timeout :
                if d(text=text, instance=index).exists:
                    d(text=text, instance=index).long_click()
                    Logger.info("click text: "+text)
                    time.sleep(1)
                    break
                else:
                    if direction=="up_down":
                        d.swipe(500, 800, 500, 200, 40)
                    if direction=="left_right":
                        d.swipe(700, 500, 100, 500, 40)
                    time.sleep(waitTime)
        else:
            d(text=text, instance=index).long_click()
            Logger.info("click text: "+text)
            self.wait(1)
    @step     
    def clickById(self,id,index=0,screeScroll=False,direction="up_down",timeout=10):
        '''
        '''
        if screeScroll==True:
            startTime=time.time()
            while time.time()-startTime<timeout:
                if d(resourceId=id, instance=index).exists:
                    d(resourceId=id, instance=index).click()
                    Logger.info("click id: "+id)
                    time.sleep(2)
                    break
                else:
                    if direction=="up_down":
                        d.swipe(500, 800, 500, 200, 40)
                    if direction=="left_right":
                        d.swipe(700, 500, 100, 500, 40)
                    time.sleep(1)
        else:
            d(resourceId=id, instance=index).click()
            Logger.info("click id: "+id)
            time.sleep(1)
    @step         
    def long_clickById(self,id,index=0,screeScroll=False,timeout=10):
        '''
        1.长按控件
        '''
        if screeScroll==True:
            startTime=time.time()
            while time.time()-startTime<timeout:
                if d(resourceId=id, instance=index).exists:
                    d(resourceId=id,instance=index).long_click()
                    Logger.info("long click id: "+id)
                    time.sleep(2)
                    break
                else:
                    d.swipe(500, 800, 500, 200, 50)
                    time.sleep(1)
        else:
            d(resourceId=id, instance=index).long_click()
            Logger.info("long click id: "+id)
            time.sleep(1)
    @step         
    def switchWidget(self,status,resourceId):
        '''
        status: "true", "false",为当前控件状态，非期望状态
        '''
        _dict={
            "关闭":"true",
            "开启":"false",
            "true":"true",
            "false":"false"
            }
        if d(checked=_dict[status],resourceId=resourceId).exists:
            d(resourceId=resourceId).click()
        else:
            Logger.info("转换开关状态为："+status)
    @step 
    def switchWighetByIndex(self, status, index=0, resourceId="amigo:id/amigo_switchWidget"):
        '''
        1,根据控件数目，转换控件，顺序 0,1,2,3...
        '''
        _dic={
            "关闭":True,
            "开启":False
            }
        if d(resourceId=resourceId)[index].info["checked"]==_dic[status]:
            d(resourceId=resourceId)[index].click()
  
    def goHome(self,times=1):
        for i in range(times):
            d.press("home")
        Logger.info("返回 Home桌面")
           
    def goBack(self,times=1):
        for i in range(times):
            d.press("back")
        Logger.info("按 Back键返回")
            
    def goBackHome(self):    
        self.goBack(3)
        self.goHome()
        
    def pressRecent(self): 
        d.press("recent") 
        
    def clearRecentApp(self):
        '''
        1.清理后台应用
        '''
        self.pressRecent()
        self.wait(0.5)
        d(resourceId="com.android.systemui:id/recent_app_clear").click()
        self.wait(2)
        Logger.info("清理后台应用")
#         self.goHome()
        
    def volumeUp(self):
        d.press("volume_up") 
        
    def volumeDown(self):
        d.press("volume_down") 
    
    def openCamera(self,toDo="picture",times=2):
        self.startActivity("com.android.camera/.CameraLauncher")
        self.clickWhenExist(className="android.widget.Button")
        self.clickWhenExist(text="继续")
        if toDo=="picture":
            for i in range(times):
                d(resourceId="com.android.camera:id/shutter_button_icon").click()
                time.sleep(2)   
    
    def putSettings(self,field,modul,mode): 
        self.shell("settings put "+field+" "+modul+" "+mode) 
    
    def installApk(self,name,mode=None):
        '''
        1.安装应用
        '''
        if mode==None:
            path=rootPath+"\\resource\\apk\\"+name
            self.adbCmd("install "+path)
        else:
            self.adbCmd("install "+mode+" install "+path)
        
    def uninstallApp(self,pkgName):
        '''
        1.卸载应用
        '''
        if self.sn==None:
            os.popen("adb uninstall "+pkgName)
            Logger.info("adb uninstall "+pkgName)
        else:
            os.popen("adb -s %s uninstall "%self.sn+pkgName)
            Logger.info("adb -s %s uninstall "%self.sn+pkgName)
    
    def allowAppPermissions(self):
        self.launchSettings() 
        self.clickByText("应用管理", screeScroll=True) 
        self.clickByText("应用权限", screeScroll=True)
        time.sleep(1)
        d.click(653, 93)
        self.clickByText("全部信任")
        self.goBack(5)
        self.goHome()
        
    def closeRotateScreen(self):
        '''
        1.关闭屏幕旋转
        '''
        d.freeze_rotation()
        
    def launchSettings(self):
        '''
        1.打开设置
        '''
        self.startActivity("com.android.settings/.GnSettingsTabActivity")
        
    def dialNum(self,numList):
        '''
        KEYCODE_HOME=3;
        KEYCODE_BACK=4;
        KEYCODE_CALL=5;
        KEYCODE_ENDCALL=6;
        KEYCODE_0=7;
        KEYCODE_1=8;
        KEYCODE_2=9;
        KEYCODE_3=10;
        KEYCODE_4=11;
        KEYCODE_5=12;
        KEYCODE_6=13;
        KEYCODE_7=14;
        KEYCODE_8=15;
        KEYCODE_9=16;
        KEYCODE_STAR=17;
        KEYCODE_POUND=18;
        '''
        KEYCODE_DIC={        
            "0":7,
            "1":8,
            "2":9,
            "3":10,
            "4":11,
            "5":12,
            "6":13,
            "7":14,
            "8":15,
            "9":16,
            "*":17,
            "#":18,
            }
        for i in numList:
            num = KEYCODE_DIC[i]
            self.shell("input keyevent "+str(num))
            time.sleep(0.5)
            
    def setTimeByUI(self): 
        localTime = str(datetime.datetime.now())
        localTime = localTime.replace("-", ":")
        localTime = localTime.replace(" ", ":")
        localTime = localTime.split(":")
        print(localTime)
        _min = localTime[4] 
        _hour = localTime[3]  
        _day = localTime[2]  
        _month = localTime[1]  
        _year = localTime[0]
        self.launchSettings()  
        self.clickByText("更多设置", screeScroll=True)
        self.clickByText("日期和时间",screeScroll=True)
        self.clickByText("设置时间")
        count=60
        while count>0:
            print(_min)
            if d.exists(text=_min):
                break
            else:
                d.swipe(466, 1006, 466, 876, 50)
                count =count - 1
                time.sleep(1)
        d.swipe(466, 1006, 466, 876, 50)
        d.swipe(466, 1006, 466, 876, 50)
        time.sleep(1)
        count1=24
        while count1>0:
            print(_hour)
            if d.exists(text=_hour):
                break
            else:
                d.swipe(253, 1006, 253, 876, 50)
                count1 =count1 - 1
                time.sleep(1)
        self.clickByText("确定")
        self.clickByText("设置日期")
        count2=31
        while count2>0:
            if d.exists(text=_day):
                break
            else:
                d.swipe(566, 1006, 566, 876, 50)
                count2 =count2 - 1
                time.sleep(1)
        count3=12
        while count3>0:
            if d.exists(text=_month):
                break
            else:
                d.swipe(359, 1006, 359, 876, 50)
                count3 =count3 - 1
                time.sleep(1)
        count4=5
        while count4>0:
            if d.exists(text=_year):
                break
            else:
                d.swipe(153, 1006, 153, 876, 50)
                count4 =count4 - 1
                time.sleep(1)
        count5=10
        while count5>0:
            if d.exists(text=_year):
                break
            else:
                d.swipe(153, 876, 153,1006 , 50)
                count5 =count5 - 1
                time.sleep(1)
        self.clickByText("确定")
        Logger.info("时间设置成功")

    def clickWhenExist(self,**keyargs): 
        '''
        1.点击符合条件的控件
        '''   
        if d(**keyargs).exists:
            self.clickObject(**keyargs)
            k = list(keyargs.keys())[0]
            v = keyargs[k]
            Logger.info("click %s : %s "%(k,v))
            time.sleep(0.5)
        else:
            pass
    @step 
    def lockScreen(self):
        '''
        1.按power键锁定屏幕
        '''
        d.press("power")
        Logger.info("锁屏")
#         self.shell("input keyevent 26")
    @step     
    def unlockScreen(self):
        '''
        1.滑动解锁手机
        '''
        
        self.wakeUp()
        self.swipe(350, 950, 350, 200, 30)
        Logger.info("解锁屏幕")
        
    def copyFile(self,filepath,toPath):
        self.adbCmd("push "+filepath+" "+toPath)
        
#         if self.sn==None:
#             os.popen("adb push "+filepath+" "+toPath)
#         else:
#             os.popen("adb -s %s push "%self.sn+filepath+" "+toPath)
            
    def pushFile(self,fileName,toPath):
        if self.sn==None:
            os.popen("adb push "+rootPath+"\\resource\\"+fileName+" "+toPath)
        else:
            os.popen("adb -s %s push "%self.sn+rootPath+"\\resource\\"+fileName+" "+toPath)
            
    def pullFile(self,fromPath,toPath):
        if self.sn==None:
            os.popen("adb pull "+fromPath+" "+toPath)
        else:
            os.popen("adb -s %s pull "%self.sn+fromPath+" "+toPath)
    
    def inputText(self, text,if_enter="0"):
        '''
        1.输入文本（中文除外）
        '''
        self.shell("input text "+text)
        if if_enter == "0":
            self.shell("input keyevent 66")
        
    def swipe(self,sx,sy,ex,ey,steps=10):
        '''
        1.滑动屏幕
        '''
        d.swipe(sx=sx, sy=sy, ex=ex, ey=ey, steps=steps)
        self.wait(0.5)
          
    def swipeToTop(self):
        '''
        1.滑动到屏幕顶端
        '''
        d.swipe(500, 300, 500, 1000, 2)
        self.wait(2)

    def swipeToBottom(self):
        '''
        1.滑动到屏幕底部
        '''
        d.swipe(500, 800, 500, 300, 2)
        self.wait(2)
        
    def drag(self,sx,sy,ex,ey,steps=10):
        '''
        1.拖动
        '''
        d.drag(sx=sx, sy=sy, ex=ex, ey=ey, steps=steps)
        
    def setDefaultIme(self,ime):
        '''
        1.设置默认输入法
        '''
        #adb shell ime list -s 可查看当前手机的输入法列表
        self.shell("ime set "+ime)
            
    def wakeUp(self):
        '''
        1.唤醒手机
        '''
        d.wakeup()
        
        
    def clearUserData(self,pkgName):
        '''
        1.清除应用数据
        '''
        self.shell("pm clear "+pkgName)
        
    def getGnVersion(self): 
        '''
        1.获取手机软件版本号
        ''' 
        sn=self.sn if self.sn !=None else "None"
        GnVersion=os.popen("adb -s %s shell getprop ro.gn.gnznvernumber" %sn).read() if sn != "None" else os.popen("adb shell getprop ro.gn.gnznvernumber").read()     
        GnVersion=GnVersion.strip()
        return GnVersion
    
    def getScreenSize(self):
        '''
        1.获取屏幕大小
        '''
        sn=self.sn if self.sn !=None else "None"
        SS=os.popen("adb -s %s shell dumpsys window displays | findstr init=" %sn).read() if sn != "None" else os.popen("adb shell dumpsys window displays | findstr init=").read()     
        SS=SS.strip().split(" ")
        SS=SS[0].split("=")
        SS=SS[1].split("x")
        X=SS[0]
        Y=SS[1]
        return int(X),int(Y)
    
    def openNotification(self):
        d.open.notification()
    
    def openQuicksetting(self):
        d.open.quick_settings()
        x,y=self.getScreenSize()
        self.swipe(0.5*x, 0.99*y, 0.5*x, 0.5*y, 20)
    
    def clickScreenCenter(self):    
        x,y=self.getScreenSize()
        self.click(0.5*x, 0.5* y)
        
    def setAirplaneMode(self, mode):
        '''
        1, 设置飞行模式, True为开启,False为关闭
        '''
        mode_dic={
            "开启":"false",
            "关闭":"true"
            }
        self.launchSettings()
        self.clickByText("更多连接")
        self.switchWidget(mode_dic[mode], "amigo:id/amigo_switchWidget")
        self.goBackHome()
#         if mode==True:
#             self.shell("settings put global airplane_mode_on 1")
#         if mode==False:
#             self.shell("settings put global airplane_mode_on 0")

    def doubleClick(self,x, y):
        '''
        1,双击坐标点
        '''
        d.double_click(x, y)
    
    def setScreenTimeout(self,timeout):
        '''
        1,设置屏幕休眠时间
        '''
        _dic={
            "30min":1800000,
            "10min":600000,
            "5min":300000,
            "2min":120000,
            "1min":60000,
            "30sec":30000,
            "15sec":15000
            }
        self.shell("settings put system screen_off_timeout "+str(_dic[timeout])) 
        
    def setText(self, id, text):
        d(resourceId=id).set_text(text)
        
    def exists(self, **keyargs):
        return d(**keyargs).exists
    
    def upgradeByOTA(self,OTA_PKG):
        self.copyFile(OTA_PKG, "/storage/sdcard0/")
        self.launchSettings()
        self.swipeToBottom()
        self.clickByText("系统升级")
        self.clickById("gn.com.android.update:id/menu_setting")
        self.clickByText("本地升级")
        self.clickByText("自动扫描更新包")
        self.clickById("gn.com.android.update:id/gn_su_id_local_fileIcon")
        self.clickByText("立即重启") 
        self.wait(2000) 
#         self.adbCmd("wait-for-device")

    def nohupTest(self, jarFile, testCase):
        self.uninstallApp("com.github.uiautomator")
        self.pushFile("jar\\"+jarFile, "/data/local/tmp/"+jarFile)
        if self.sn==None:
            cmd="adb shell uiautomator runtest "+jarFile+" --nohup -c com.power.test.testCase#"+testCase
        else:
            cmd="adb -s %s "%self.sn+"shell uiautomator runtest "+jarFile+" --nohup -c com.power.test.testCase#"+testCase
        print(cmd)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)
    
    def clickWatcher(self, *args, **keyargs):
        watcherName=str(*args)
        d.watcher(watcherName).when(**keyargs).click(**keyargs)
        return watcherName
#         print(d.watchers)
#         print(d.watchers.triggered)       
    def removeWatcher(self, name):
        d.watcher(name).remove() 
        print(d.watchers)   
        
if __name__=="__main__":
#     Common().clickWatcher("CON",text="继续")
#     Common().clickByText("123")
    print(Device().watchers)   
    Common().removeWatcher("TEST") 