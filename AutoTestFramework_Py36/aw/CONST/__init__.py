#-*- coding:utf-8 -*-
'''
Created on 2016.11.25

@author: 杨立凯
'''
class LOOP(object):
    global LOOP
    loop1 = 1
    loop2 = 2
    loop100 = 100
    loop200 = 200
    
class POWER(object):
    
    sample = 100
    Vout = 4.0
    delay = {
        0:0,
        10:10,
        60:60,
        180:180,
        300:300
        }
    tPath = "D:\\PowerResult\\"
    
class WIFI(object):
    SSID="gionee_staff"
    password="Gionee@520"