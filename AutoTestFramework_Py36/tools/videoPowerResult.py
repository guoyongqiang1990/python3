#-*- coding:utf-8 -*-
import os,sys
import time
from datetime import datetime
#adb pull /storage/sdcard0/BatteryLog.csv d:\
def deltaTime(a,b):
    delta = (datetime.strptime(a,'%H:%M:%S')-datetime.strptime(b,'%H:%M:%S')).seconds
    h = delta//3600
    m = (delta%3600)//60
    s = delta-h*3600-m*60
    return ":".join([str(h),str(m),str(s)])

os.popen(r"adb pull /storage/sdcard0/BatteryLog.csv "+os.path.abspath(os.path.dirname(__file__)))
f=open("BatteryLog.csv","r")
# r=file("result.csv","w")
# r.write("100%_time,_v,90%_time,_v,dif,80%_time,_v,dif,70%_time,_v,dif,60%_time,_v,dif,50%_time,_v,dif,40%_time,_v,dif,30%_time,_v,dif,20%_time,_v,dif,10%_time,_v,dif,1%_time,_v,0%_time,_v,dif\n")
# r.close()
for line in f.readlines():
    line = line.strip("\n").split(" ")
    line = line[-1].split(",")
    rtime = line[0]
    level = line[1]
    voltage = line[3]
    status = line[4]
    if status =="\"Use\"":
        if int(level) ==100:
            time_100 = rtime
            voltage_100 = voltage
        elif int(level) ==90:
            time_90 = rtime
            voltage_90 = voltage
            delta90_100 = deltaTime(time_90, time_100)
        elif int(level) ==80:
            time_80 = rtime
            voltage_80 = voltage
            delta80_90 = deltaTime(time_80, time_90)
        elif int(level) ==70:
            time_70 = rtime
            voltage_70 = voltage
            delta70_80 = deltaTime(time_70, time_80)
        elif int(level) ==60:
            time_60 = rtime
            voltage_60 = voltage
            delta60_70 = deltaTime(time_60, time_70)
        elif int(level) ==50:
            time_50 = rtime
            voltage_50 = voltage
            delta50_60 = deltaTime(time_50, time_60)
        elif int(level) ==40:
            time_40 = rtime
            voltage_40 = voltage
            delta40_50 = deltaTime(time_40, time_50)
        elif int(level) ==30:
            time_30 = rtime
            voltage_30 = voltage
            delta30_40 = deltaTime(time_30, time_40)
        elif int(level) ==20:
            time_20 = rtime
            voltage_20 = voltage
            delta20_30 = deltaTime(time_20, time_30)
        elif int(level) ==10:
            time_10 = rtime
            voltage_10 = voltage
            delta10_20 = deltaTime(time_10, time_20)
        elif int(level) ==1:
            time_1 = rtime
            voltage_1 = voltage
        elif int(level) ==0:
            time_0 = rtime
            voltage_0 = voltage
            delta0_10 = deltaTime(time_0, time_10)
            delta0_1 = deltaTime(time_0, time_1)
            delta0_100 = deltaTime(time_0,time_100)
with file("result.csv","a") as r:
    r.write(",".join([time_100,voltage_100,time_90,voltage_90,delta90_100,time_80,voltage_80,delta80_90,
                      time_70,voltage_70,delta70_80,time_60,voltage_60,delta60_70,time_50,voltage_50,delta50_60,
                      time_40,voltage_40,delta40_50,time_30,voltage_30,delta30_40,time_20,voltage_20,delta20_30,
                      time_10,voltage_10,delta10_20,time_1,voltage_1,time_0,voltage_0,delta0_10,delta0_1,delta0_100,"\n"]))    
f.close()