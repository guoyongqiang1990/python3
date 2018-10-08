# -*- coding: utf-8 -*-
__author__ = 'liliang'

from pyh import *
import getLogData

def getdata():
    all=[]
    log=[]
    scriptpara=[]
    byte_string=[]
    tmp=[]
    tmp1=[]
    logdata=[]
    data=getLogData.getmanylogdata("/Users/liliang/Documents/workspace/PycharmProjects/android")
    temp=''
    count=1
    j=1
    for i in data:
        print 'data::',len(data)
        #print 'i:::',i
        if type(i[1])==list:
            keys1= i[0].keys()
            values1=i[0].values()
            len1= len(i[0].keys())
            print 'len1:::',len1

            for j in range(len1):
                print 'count::',count
                temp+=('<Br>' +'Device'+str(count)+ ': '+str(keys1[j]) + ' <Br>  '+str(values1[j]))
                print 'temp::',temp

            tmp.append(temp)
            tmp1.append(tmp)
            count+=1

            logdata.append(tmp)
            log.append(i[0])
            if len(i[1])==5:

                scriptpara.append(i[1])

    all.append(scriptpara)
    all.append(tmp1)
    return all

def getdatamethod():
    all=[]
    log=[]
    scriptpara=[]
    byte_string=[]
    tmp=[]
    tmp1=[]
    logdata=[]
    data=getLogData.getmanylogdata("/Users/liliang/Documents/workspace/PycharmProjects/android")
    temp=''
    temp1=''
    count=1
    print data
    for i in range(len(data)):
        print 'i temp :',i,temp
        for j in range(len(data[i][0].keys())):
            print 'j', j
            temp+=('<Br>' +'Device'+str(count)+ ': '+str(data[i][0].keys()[j]) + ' <Br>  '+str(data[i][0].values()[j]))
        print '1111temp1111:',temp
        temp1=temp
        tmp.insert(i,temp1)
        print 'tmp:::',tmp
        temp=''
        temp1=''
        tmp1.append(tmp)
        print 'tmp1:::',tmp1
        count+=1

        if len(data[i][1])==5:
            scriptpara.append(data[i][1])

    #log.append(scriptpara)
    all.append(tmp1[-1])
    all.append(scriptpara)
    print 'tmp1:::all:::',all
    print 'tmp1:::scriptpara:::',log
    return all





#make html
def maketohtml(list,byte_string=[]):
    page = PyH('MonkeyLogAnalysis')
    page << h1('Monkey Log Analysis', align='center')
    #set table
    mytab = page << table(width="100%",border="1",cellpadding="3",cellspacing="0",style="margin:auto",align='center')
    tr1 = mytab << tr(bgcolor="lightgrey")
    tr1 << th('DeviceName')+ th('Seed')+th('Count')+th('PackageName') +th('Pass/Fail')
    for i in range(len(list)):
        #print len(list)
        tr2 = mytab << tr()
        for j in range(5):
            tr2 << td(list[i][j])
            if list[i][j]=='Pass':
                tr2[4].attributes['bgcolor']='Green'

            if list[i][j]=='Fail':
                tr2[4].attributes['bgcolor']='red'

    data=[byte_string]
    print 'data::::',data
    page<<div(style="text-align:letf")<<h2('Log: ')
    mytab = page << table(width="100%",border="0",cellpadding="3",cellspacing="0",style="margin:auto",align='left')
    print 'data[0]::::', data[0]
    for i in range(len(data)):
        tr2 = mytab << tr()
        for j in range(1):
            tr2 << td(data[j])

    page.printOut('test.html')


list=getdatamethod()
print 'list0::::',list[0]
maketohtml(list[1],list[0])
