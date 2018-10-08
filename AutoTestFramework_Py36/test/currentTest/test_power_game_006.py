#-*- coding:utf-8 -*-
'''
用例标题：
测试步骤：
1.进入捕鱼达人3
2.判断升级重启提示
3.开始、出发
4.判断是否有领取
5.每10秒点击一次屏幕
6.重复步骤4、5，执行75次
7.返回待机
预期结果：

'''
from aw import *
from aw.power import USB,PM 
######################################             
TAG=__file__.split("\\")[-1]
TAG = TAG.split('.')[0]                  
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).unlockScreen()
        Common(DUT).clearRecentApp()
    def test_step(self):
        Common(DUT).clickByText("捕鱼达人3", screeScroll=True, direction="left_right")
        Common(DUT).wait(12)
        Common(DUT).click(960,850)
        Common(DUT).wait(2)
        Common(DUT).click(1581,852)
        Common(DUT).wait(5)
        Common(DUT).click(760,754)
        Common(DUT).click(1638,294)
 
        Common(DUT).nohupTest("PowerTestCases.jar", "testGame")
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=180, caseName=TAG)
        PM.powerMeasure(sample=100, mTime=750, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
 
    def tearDown(self):
        Common(DUT).wait(10)
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
