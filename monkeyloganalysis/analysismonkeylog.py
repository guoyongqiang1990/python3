# -*- coding: utf-8 -*-
__author__ = 'liliang'

import re
import os
import sys


def getfile(path):
    filelist=[]
    for file in os.listdir(path):
        if re.search('monkeylog',file) and re.search('.txt$',file):
            #print 'file: '+file
            file_path = os.path.join(path, file)
            filelist.append(file_path.decode('utf-8'))
    return filelist



def getData(filename):
    tmp=''
    f = open(filename,"r")
    lines = f.readlines()
    count=0
    anrcount=0
    crashcount=0
    exceptioncount=0
    nullcount=0

    dictlog={}
    scriptpara=[]
    alldata=[]

    #获取设备名
    scriptpara.append(filename[filename.rfind("/")+1:filename.rfind("monkeylog")])
    for line in lines:
        if re.search('anr', line, re.IGNORECASE):
            a=lines.index(line)
            anrcount +=1
            for var in range(a-5,a+5):
                tmp+=lines[var]
            couanr='ANR'+str(anrcount)
            dictlog[couanr]=tmp

        elif re.search('crash', line, re.IGNORECASE):
            a=lines.index(line)
            crashcount +=1
            for var in range(a-5,a+5):
                tmp+=lines[var]
            couanr='Crash'+str(crashcount)
            dictlog[couanr]=tmp

        elif re.search('java.lang.NullPointerException', line, re.IGNORECASE):
            a=lines.index(line)
            exceptioncount +=1
            for var in range(a-5,a+5):
                tmp+=lines[var]
            couanr='Exception'+exceptioncount
            dictlog[couanr]=tmp
        elif re.search('java.lang.IllegalStateException', line, re.IGNORECASE):
            a=lines.index(line)
            exceptioncount +=1
            for var in range(a-5,a+5):
                tmp+=lines[var]
            couanr='Exception'+exceptioncount
            dictlog[couanr]=tmp
        elif re.search('java.lang.IllegalArgumentException', line, re.IGNORECASE):
            a=lines.index(line)
            exceptioncount +=1
            for var in range(a-5,a+5):
                tmp+=lines[var]
            couanr='Exception'+exceptioncount
            dictlog[couanr]=tmp
        elif re.search('java.lang.ArrayIndexOutOfBoundsException', line, re.IGNORECASE):
            a=lines.index(line)
            exceptioncount +=1
            for var in range(a-5,a+5):
                tmp+=lines[var]
            couanr='Exception'+exceptioncount
            dictlog[couanr]=tmp
        elif re.search('java.lang.RuntimeException', line, re.IGNORECASE):
            a=lines.index(line)
            exceptioncount +=1
            for var in range(a-5,a+5):
                tmp+=lines[var]
            couanr='Exception'+exceptioncount
            dictlog[couanr]=tmp

        elif re.search('java.lang.SecurityException', line, re.IGNORECASE):
            a=lines.index(line)
            exceptioncount +=1
            for var in range(a-5,a+5):
                tmp+=lines[var]
            couanr='Exception'+exceptioncount
            dictlog[couanr]=tmp




        #获取脚本参数
        elif re.search('AllowPackage:', line, re.IGNORECASE):
            a=lines.index(line)
            scriptpara.append(line[line.rfind("AllowPackage:")+14:line.rfind('\r')])
        elif re.search('seed=', line, re.IGNORECASE):
            a=lines.index(line)
            scriptpara.append(line[line.rfind("seed=")+5:line.rfind(' ')])
            scriptpara.append(line[line.rfind("count=")+6:line.rfind('\r')])
    f.close()
    count=anrcount+crashcount+exceptioncount
    if count>0:
        scriptpara.append('Fail')
    else:
        scriptpara.append('Pass')
    if len(scriptpara)<3:
        print filename,'脚本没有执行，不做记录！！！'
    elif len(scriptpara)<5:
        scriptpara.insert(1,'')
        scriptpara.insert(2,'')
        alldata.append(dictlog)
        alldata.append(scriptpara)
    elif len(scriptpara)==5:
        alldata.append(dictlog)
        alldata.append(scriptpara)
    return alldata


#获取多文件的log数据
def getmanylogdata(path):
    log=[]

    arr=getfile(path)
    for i in arr:
        if re.search('monkeylog',i) and re.search('.txt$',i):
            if getData(i)!=[]:
                log.append(getData(i))
    return log




#arr=getfile("/Users/liliang/Documents/workspace/PycharmProjects/android")
#tmp = getData("/Users/liliang/Documents/workspace/PycharmProjects/android/乐视超级手机1monkeylog20170814175957.txt")
getmanylogdata("/Users/liliang/Documents/workspace/PycharmProjects/android")
