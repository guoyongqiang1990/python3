#-*- coding:utf-8 -*-
'''
Created on 2016.11.25

@author: 杨立凯
'''
import time
import json
import os,sys
import unittest
from functools import reduce 
from logger import Logger
from uiautomator import Device

from PIL import Image
import math
import operator

def check(func):
    def wrapper(*args,**kwargs):
        flag = func(*args,**kwargs)
        if Checkpoint().logConfig("log")=="on":
            if flag == True and Checkpoint().logConfig("pass")=="off":
                pass
            else:
                Checkpoint().catchLog()
        return flag
    return wrapper

class checkPointResult(Exception):
    pass
            
class Checkpoint(object):
    def __init__(self,sn=None):
        global d
        d=Device(sn)
        self.sn=sn
        self.rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        self.record = time.strftime("%Y-%m-%d_%H-%M-%S") 
    
    def logConfig(self,item):
        jsonFile="project.json"
        with open(self.rootPath+"\\"+jsonFile,"r") as f:
            DATA = json.load(f)
        config=DATA["log_config"][item]
        return config
            
    def catchLog(self):
        with open(self.rootPath+"\\project.log","r") as f:
            savePath = f.readline().strip()
        if self.logConfig("log")=="on":
            logPath=savePath+"\\log_"+self.record
            Logger.info("===正在抓取LOG===")
            if not os.path.exists(logPath):
                os.makedirs(logPath)
            sn=self.sn if self.sn !=None else "None"
            hwinfo=os.popen("adb -s %s shell getprop ro.hardware" %sn).read() if sn != "None" else os.popen("adb shell getprop ro.hardware").read()
            hwinfo=hwinfo.strip()
    #         print hwinfo
            if "qcom" in hwinfo:
                os.system(self.rootPath+"\\tools\\catchlog_qc.bat "+sn+" "+logPath)
            if "mt" in hwinfo:
                os.system(self.rootPath+"\\tools\\catchlog_mt.bat "+sn+" "+logPath)
            Logger.info("===LOG抓取完成===")
        else:
            pass
    
    @check            
    def checkIfExist(self,message,**keyargs):
        '''
        1.检查控件是否存在（text， id等）
        '''
        key=list(keyargs.keys())[0]
        print("$$$$$$$$$$$$$$$$")
        value=keyargs[key]
        print(keyargs)
        print(key)
        Logger.info(message+":")   
        if not d.exists(**keyargs):
            Logger.error("Failed, %s "%key+":"+"\"%s\" not exist in current window"%value)
            return False
        else:
            Logger.info("Pass,属性%s "%key+":"+"\"%s\" 存在于当前页面"%value)
            return True
        
    @check         
    def checkIfNotExist(self,message="",**keyargs):
        key=list(keyargs.keys())[0] 
        value=keyargs[key]
        print(message+":")   
        if not d.exists(**keyargs):
            Logger.info("Pass,属性%s "%key+":"+"\"%s\" 不存在于当前页面"%value)
            return True
        else:
            Logger.error("Failed, %s "%key+":"+"\"%s\"  exist in current window"%value)
            return False
        
    @check
    def checkIfTextExistBySwipe(self,message="",text="",direction="up_down",timeout=10):
        print(message+":") 
        startTime=time.time()
        while time.time()-startTime<timeout :
            if d(text=text).exists:
                Logger.info("text: "+text+" exist in current window")
                time.sleep(1)
                return True
                break
            else:
                if direction=="up_down":
                    d.swipe(500, 800, 500, 200, 50)
                if direction=="left_right":
                    d.swipe(700, 500, 100, 500, 30)
                time.sleep(1.5)
        else:
            Logger.error("text: "+text+" not exist in current window")
            return False
    
    def imageSimilarity(self, image2):
        
        image1=self._screenShot()
        image2=self.rootPath+"\\resource\\image\\"+image2
        
        image1 = Image.open(image1)
        image2 = Image.open(image2)
        h1 = image1.histogram()
        h2 = image2.histogram()
        SV = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
        print(SV)
        return SV
    
    @check
    def checkImage(self, standardImage, similar=0.99):
        '''
        1.图片对比
        '''
        _dic={
            1 : 0,
            0.99 : 10,
            0.9 : 50,
            }
        
        if self.imageSimilarity(standardImage) > _dic[similar]:
            Logger.error("Fail,图片对比失败")
            return False
        
        else:
            Logger.info("pass,图片对比成功")
            return True
        
# Checkpoint().checkImage('adc.png')