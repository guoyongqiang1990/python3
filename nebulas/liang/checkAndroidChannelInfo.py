# -*- coding: utf-8 -*-
__author__ = 'MrLi'

###############################
#
#使用aapt验证渠道信息
#
#
###############################

import os
import csv
import platform
from subprocess import Popen,PIPE
import sys
from xml.etree import ElementTree
from os.path import join
import re
import time
import shutil


passPackage = []
failPackage = []
total = []
count = []

def main(SRC_DIR):
    list = os.listdir(SRC_DIR)
    filelist = []
    website = []
    for i in range(0,len(list)):
    	path = os.path.join(SRC_DIR,list[i])
    	if os.path.isfile(path) and path.find('cn.buding.martin') != -1 and (os.path.isdir(path)) != True:
    		filelist.append(path)
        elif os.path.isfile(path) and path.find('.apk') != -1 and (os.path.isdir(path)) != True:
            website.append(path)
    getApkPackageChannelInfo(SRC_DIR,filelist,'channel')
    getApkPackageChannelInfo(SRC_DIR,website,'website')
    print printdecodemethod('验证成功的渠道包:  '),passPackage.__len__()
    print printdecodemethod('验证失败的渠道包:  '),failPackage.__len__(),failPackage
    print printdecodemethod('渠道包总数量: '),count[count.__len__()-1]+count[0]
    total = failPackage+passPackage
    writecsv(passPackage.__len__(),failPackage.__len__(),count[count.__len__()-1]+count[0],total)


def getApkPackageChannelInfo(SRC_DIR,list,apkorwebsite):
    packageinfo = ""
    if apkorwebsite == "channel":
        count.append(list.__len__())
        os.chdir(SRC_DIR)
        for i in range(0,len(list)):
            try:
                packageinfo = list[i].split("__")[1]
                print i+1
                apkinfo = getChannelInfo(list[i],packageinfo)
                if apkinfo[8]=='pass':
                    passPackage.append(apkinfo)
                else:
                    failPackage.append(apkinfo)
            except Exception:
                print '\nplease check package name!',list[i],'\n'
    elif apkorwebsite == "website":
        count.append(list.__len__())
        for j in range(0,len(list)):
            try:
                [dirname,packagename] = os.path.split(list[j])
                if packagename != 'weiche.apk':
                    packageinfo=list[j].split("weiche_")[1].split(".")[0]
                    packageinfo="website_"+packageinfo
                    print count[0]+j+1
                else:
                    packageinfo = "website"
                    print count[0]+j+1
            except Exception:
                print "please check package name!"
            websiteinfo = getChannelInfo(list[j],packageinfo)
            if websiteinfo[8]=='pass' and websiteinfo[3]=="online" and websiteinfo[6]=="false" and websiteinfo[7]=="debug_off":
                passPackage.append(websiteinfo)
            else:
                failPackage.append(websiteinfo)


def getChannelInfo(apkpath,packageinfo):
    configinfo = []
    if platform.system() == "Windows":
        command = 'aapt l ' + apkpath + ' | findstr "^META-INF/.*@weiche.cn$" '
    else:
        command = 'aapt l ' + apkpath + ' | grep ^META-INF/.*@weiche.cn$'
        #linux or unix等可使用获取完整字符串
        #command = 'aapt l ' + apkpath + ' | grep ^META-INF/.*@weiche.cn$ | cut -b 10-'+ " | awk -F '@' '{print $1}' "
    try:
        temp = Popen(command,shell=True,stdout=PIPE)
        channelinfoinapk = temp.communicate()[0].split("\r\n")[0]
        channelinfoinapk = channelinfoinapk.split("META-INF/")[1].split("@weiche.cn")[0]

    except Exception as err:
        print "please check,add adb and aapt to environment path!!!"
    finally:
        [dirname,packagename] = os.path.split(apkpath)
        configinfo = decompilationApk(apkpath,dirname,packageinfo,30)

    packagename=apkpath.split("/")[-1]
    if channelinfoinapk == packageinfo:
        result = 'pass'
    else:
        print "***********check fail !!!**************"
        result = 'fail'

    print 'ApkName: ',packagename
    print 'channelinfoinapk: ',channelinfoinapk
    print 'ChannelPackageinfo:',packageinfo
    print 'api_env: ',configinfo[0]
    print 'log_enable: ',configinfo[3]
    print 'sensors_environment: ',configinfo[4]
    print 'ChannelInfoCheckResult: ',result
    print 'app_key_online: ',configinfo[1]
    print 'app_secret_online: ',configinfo[2]

    print
    apkinfo = [packagename,channelinfoinapk,packageinfo]+configinfo+[result]
    return apkinfo

def writecsv(checkpass,checkfail,total,data):
    file2 = '../channelcheckresult.csv'
    with open(file2, 'w') as f:
        writer = csv.writer(f)
        writer.writerow([decodemethod('渠道包验证通过数量','gbk'), checkpass])
        writer.writerow([decodemethod('渠道包验证失败数量','gbk'), checkfail])
        writer.writerow([decodemethod('渠道包总数量','gbk'), total])
        writer.writerow(['ApkName','ChannelInfoInApk','PackageInfo','api_env','app_key_online','app_secret_online','log_enable','sensors_environment','CheckResult'])
        for row in data:
            writer.writerow(row)

def decodemethod(str,encodestr):
    encodestr = str.decode("utf-8").encode(encodestr)
    return encodestr
def printdecodemethod(str):
    type = sys.getfilesystemencoding()
    strrs = decodemethod(str,type)
    return strrs




def decompilationApk(file,dir,filename,wailtime):
    result = []
    os.chdir(dir)
    if platform.system() == "Windows":
        command = 'apktool -s d ' + file.replace("\\","\\\\") + ' -o '+ filename
    else:
        command = 'apktool -s d ' + file + ' -o '+ filename
    try:
        temp = Popen(command,shell=True,stdout=PIPE)
    except Exception:
        print "please check filename or ",filename," !"
    try:
        time.sleep(wailtime)
        targetfile = getTargetFile(dir,filename)
        result = parseXmlChannelInfo(targetfile)
    except Exception:
        print 'please check ,whether to uppack!'
    return result


def parseXmlChannelInfo(file):
    with open(file,'rt') as f:
        tree = ElementTree.parse(f)
    result=[]
    root = tree.getroot()
    child = root.getchildren()
    for i in child:
        #print i.text,i.attrib['name'],i.tag,i.tail
        if i.attrib['name'] == 'api_env':
            result.append(i.text)
        elif i.attrib['name'] == 'app_key_online':
            result.append(i.text.split('=')[0])
        elif i.attrib['name'] == 'app_secret_online':
            result.append(i.text.split('=')[0])
        elif i.attrib['name'] == 'log_enable':
            result.append(i.text)
        elif i.attrib['name'] == 'sensors_environment':
            result.append(i.text)
    return result

def getTargetFile(dir,filename):
    file = ''
    for root, dirs, files in os.walk(dir):
        pattern = re.compile(r'.*values$')
        m  = pattern.match(root)
        if m != None:
            file = join(root,'strings.xml')
            #print m,files,file
    return file

def removedirall(dir):
    shutil.rmtree(dir)

def removedir(dir):
    filedir = []
    if os.path.isdir(dir):
        files = os.listdir(dir)
        for i in files:
            file = os.path.join(dir,i)
            if os.path.isdir(file):
                filedir.append(file)
                removedirall(file)





if __name__ == '__main__':
    from sys import argv
    filepath = argv[1]
    main(filepath)
    (superdir,dirname) = os.path.split(filepath)
    print printdecodemethod('生成的结果文件： '),os.path.join(superdir,'channelcheckresult.csv')
    #delete dirs
    try:
        time.sleep(30)
        delpara = argv[2]
        if delpara == 'del':
            removedirall(filepath)
    except Exception:
        removedir(filepath)


