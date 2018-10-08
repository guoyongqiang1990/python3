#-*- coding:utf-8 -*-
'''
用例标题：
测试步骤：
1.进入百度首页，点击新闻
2.判断刷新按钮，上限5次
3.每10s向上滑动并刷新一次
4.重复2、3步66次
预期结果：

'''
from aw import *
from aw.power import USB,PM 
######################################             
TAG=__file__.split("\\")[-1]
TAG = TAG.split('.')[0]                  
######################################
class TestScript(unittest.TestCase):
        
    def test_step(self):

        Common(DUT).setScreenTimeout("30min")
        Common(DUT).installApk("buyudaren3.apk")
        Common(DUT).pushFile("Reader.txt", "/storage/sdcard0/")   

if __name__ == "__main__":
    unittest.main()
