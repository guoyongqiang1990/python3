#-*- coding:utf-8 -*-
whiteList=[]
lines = open('testResult.xml').readlines()  
fp = file('test_result2.xml','w')  
for line in lines:
    if "<Failure" in line:
        line=""
    if "</Failure>" in line:
        line=""
    elif "<StackTrace" in line :
        line=""
    elif "</StackTrace>" in line :
        line=""
    elif "<FailedScene" in line :
        line=""
    elif "</FailedScene>" in line :
        line=""
#     elif "</Test>" in line:
#         line=""
    elif "<" not in line:
        line=""
    if "result=\"fail\"" in line and "/>" not in line: 
        line=line.replace("fail","pass")#.replace(">","/>")  
    fp.write(line)
print "over"
fp.close()  