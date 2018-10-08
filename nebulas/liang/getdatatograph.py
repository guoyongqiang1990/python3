# -*- coding:utf-8 -*-
__author__ = 'liliang'
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import glob


def getdata(filepath):

 with open(filepath,'rU') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    file = open(filepath)
    numline = len(file.readlines())

    time=[]
    memory=[]
    cpu=[]
    traff=[]
    battery=[]
    device = ""
    i = 0

    for row in reader:
        i+=1
        if(i>9)&(i<numline-4):
            memory.append(row[3])
            cpu.append(row[5])
            traff.append(row[11])
            battery.append(row[12].rstrip('%'))
        elif(i==6):
               device=row[1]
    file.close()
    return memory,cpu,traff,battery,device

def getonegraph(arr):
    y = arr
    plt.figure(figsize=(8,4))
    plt.plot(y,label="test")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("PyPlot First Example")
    plt.legend()
    plt.show()





def getmanycsvgraph(arr):
    y = arr
    plt.figure(figsize=(8,4))
    plt.plot(y,label="test")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("PyPlot First Example")
    plt.legend()
    plt.show()



def getgetmanygraph(t1,t2,t3,t4,t5):
    plt.figure(figsize=(12,6))
    plt.subplot(411)             
    plt.plot(t1)
    plt.ylabel("Memory(M)",rotation='horizontal',horizontalalignment='right')

    plt.subplot(412)             
    plt.plot(t2)
    plt.ylabel("CPU(%)",rotation='horizontal',horizontalalignment='right')

    plt.subplot(413)             
    plt.plot(t3)
    plt.ylabel("Traffic(KB)",rotation='horizontal',horizontalalignment='right')

    plt.subplot(414)             
    plt.plot(t4)
    plt.ylabel("Battery(%)",rotation='horizontal',horizontalalignment='right')


    plt.figure(1)                
    plt.subplot(411)             
    plt.title('cn.buding.martin ('+ t5+")")

    path = sys.argv[1]+t5+".png"
    plt.savefig(path,dpi=600)



filepath=sys.argv[2]
def getmanygraph():
    list = os.listdir(filepath)
    filelist = []
    for i in range(0,len(list)):
          path = os.path.join(filepath,list[i])
          if os.path.isfile(path) and path.find('.csv') != -1 and (os.path.isdir(path)) != True:
              filelist.append(path)
    print filelist
    for i in range(0,len(filelist)):
        temp = getdata(filelist[i])
        getgetmanygraph(temp[0],temp[1],temp[2],temp[3],temp[4])


getmanygraph()





