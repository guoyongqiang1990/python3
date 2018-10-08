#-*- coding:utf-8 -*-
import os
import time
recordTime=time.strftime("%Y-%m-%d_%H-%M-%S")
resultFile="result"+recordTime+".csv"
r=open(resultFile,"w")
r.write("CASENAME,AVG CURRENT,MIN CURRENT,MAX CURRENT\n")
r.close()
# 设置功耗测试结果存放路径
resultPath=r"D:\PowerResult"
for root,dirs,files in os.walk(resultPath):
    for file in files:
        fileName=file.split("\\")[-1]
        caseName=fileName.split(".csv")[0]
#         print caseName
        rf=open(resultPath+"\\"+caseName,"r")
        avg_list=[]
        min_list=[]
        max_list=[]
        for line in rf.readlines()[1:]:
            values=line.split(",")
            AvgCurrent=float(values[1])
            MinCurrent=float(values[4])
            MaxCurrent=float(values[7])
            avg_list.append(AvgCurrent)
            min_list.append(MinCurrent)
            max_list.append(MaxCurrent)
        
        r_avg=reduce(lambda x,y: x+y, avg_list)/len(avg_list)
        r_min=reduce(lambda x,y: x+y, min_list)/len(min_list)
        r_max=reduce(lambda x,y: x+y, max_list)/len(max_list)
        
        r=open(resultFile,"a")
        r.write(caseName+","+str(r_avg)+","+str(r_min)+","+str(r_max)+"\n")