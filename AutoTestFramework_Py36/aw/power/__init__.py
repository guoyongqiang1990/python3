#-*- coding:utf-8 -*-
import shutil
try:
    import visa
except ImportError:
    print("import visa module failed")
import time
import os
import ctypes
from functools import reduce 
from aw.common import Common
from logger import Logger

class USBcontrol:
    def __init__(self):
        resDict={
            0:"成功",
            1:""}
        self.resDict = resDict
        dllPath = os.path.abspath(os.path.dirname(__file__))
        self.objdll = ctypes.windll.LoadLibrary(dllPath+r'\usbplug.dll')
        self.hdl = self.objdll.USBPLUG_Open(1)
#         print "open handle = " + str(self.hdl)
        
    def connectUsb(self):
        return
        res = self.objdll.USBPLUG_Set(self.hdl, 1) #连接USB
        os.system("adb wait-for-device")
        Logger.info("连接 USB " + self.resDict[res])
    def disconnectUsb(self):
        return
        res = self.objdll.USBPLUG_Set(self.hdl, 0) #断开USB
        Logger.info("断开 USB " + self.resDict[res])
#     def __del__(self):
#         res = self.objdll.USBPLUG_Close(self.hdl)
#         print("close handle = "+str(self.hdl) +" "+ self.resDict[res])
class Power(object):
    def __init__(self,gpib='GPIB0::5::INSTR'):
        self.gpib = gpib
#         RM = visa.ResourceManager()
#         self.inst = RM.open_resource(self.gpib)
#         self.resList = RM.list_resources()
#         self._cmd("*RST")
#         self._cmd("*CLS")
#         self._cmd("STAT:PRES")
#         self._cmd("*SRE 0")
#         self._cmd("ESE 0")
         
    def _cmd(self,cmd):    
        return self.inst.write(cmd)
    
    def setVoltage(self,value):
        return self._cmd("VOLT "+value)
    
    def setCurrent(self,value):
        return self._cmd("CURR "+value)
    
    def setOutPut(self,status="ON"):
        return self._cmd("OUTP "+status)
    
    def measureCurrent(self):
        return float(self.inst.query("MEAS:CURR?"))
    
    def powerMeasure(self,sample=10,mTime=10,Vout=4.0,delay=0,caseName="test_demo",fPath="E:\\workspace\\GN_AutoTest", tPath="D:\\"):
        return
        self.setVoltage(str(Vout))
        self.setOutPut("ON")
        Logger.info("开始采集电流数据")
        record = time.strftime("%Y-%m-%d_%H-%M-%S")
        resultFile = tPath+caseName+"_"+record+".csv"
        with open(resultFile,"w") as f:
            f.write("TIME,CURRENT(mA)\n")
            time.sleep(delay)
            startTime=time.time()
            count=0
            _sum=0
            while time.time()-startTime<mTime:
                current = self.measureCurrent()
#                 current = current
#                 count = count +1
#                 _sum = _sum+current
#                  avg = _sum/count
                f.write("%s,%.5f\n"%(str(time.strftime("%H:%M:%S")),current*1000))
        Logger.info("电流数据保存到："+resultFile)
        summaryFile=tPath+"result_summary.csv"
        if not os.path.isfile(summaryFile):
            with open(summaryFile,"w") as s:
                s.write("CASENAME,AVG CURRENT(mA),MIN CURRENT(mA),MAX CURRENT(mA)\n")
        with open(resultFile,"r") as rf:
            avg_list=[]
            for line in rf.readlines()[1:]:
                values=line.split(",")
                AvgCurrent=float(values[1])
                avg_list.append(AvgCurrent)
         
        r_avg=reduce(lambda x,y: x+y, avg_list)/len(avg_list)
        r_min=avg_list[0]
        for i in avg_list[1:]:
            if(r_min>i):
                r_min=i
        r_max=avg_list[0]
        for i in avg_list[1:]:
            if(r_max<i):
                r_max=i    
        with open(summaryFile,"a") as s:
            s.write(caseName+","+str(r_avg)+","+str(r_min)+","+str(r_max)+"\n")

        
class PowerMonitor(object):  
    def __init__(self):
        self.path_PMtool= os.path.abspath(os.path.dirname(__file__))
#         print self.path_PMtool  

    def powerMeasure(self,sample=10, mTime=10,Vout=3.8, delay=1,caseName="test", fPath="E:\\workspace\\GN_AutoTest", tPath="D:\\"):
        # trigger=ETY10D20A :开始条件E：立即开始;T:条件分割标识;Y10:每隔10个sample 记录一个数据;D20A:采集数据时长20s,A代表秒
        time.sleep(delay)
        Logger.info("开始采集电流数据")
        recordTime=time.strftime("%Y-%m-%d_%H-%M-%S")
        resultFile=caseName+"_"+recordTime
        cmd=self.path_PMtool+"\PowerToolCmd /savefile="+resultFile+".pt5 /trigger=ETY"+str(sample)+"D"+str(mTime)+"A /vout="+str(Vout)+" /keeppower /noexitwait"
#         print cmd
        exit_code=os.popen(cmd).read()
        flag="Exit Code [0] (Success)"
        startTime=time.time()
        while flag not in exit_code:
            exit_code=os.popen(cmd).read()
            time.sleep(2)
            if time.time()-startTime>120:
                break
        print (exit_code)
        resultPath=os.getcwd()+"\\"+resultFile+".csv"
        tPath=tPath
        if not os.path.exists(tPath):
            os.makedirs(tPath)
        if os.path.isfile(resultPath):
            shutil.move(resultPath, tPath)
            Logger.info("电流数据保存到："+tPath)

USB=USBcontrol()
PM=Power()

if __name__ == "__main__":
    USB.connectUsb()
