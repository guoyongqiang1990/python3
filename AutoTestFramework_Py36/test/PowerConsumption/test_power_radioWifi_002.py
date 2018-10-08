#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：
1,飞行模式开启
2,WIFI关闭
3,GPS关闭
4,BT开启
测试步骤：
1.3分钟后测试待机电流10分钟
预期结果：

'''
from aw import * 
from aw.power import USB,PM 
# from aw.power import Power,USB 
######################################             
TAG=__file__.split("\\")[-1]      
fPath=rootPath+"\\"+TAG         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Setting(DUT).switchAirplane("开启")
        Setting(DUT).switchWifi("开启")
        Setting(DUT).switchGPS("关闭")
        Common(DUT).goBackHome()
        Common(DUT).clearRecentApp()
    def test_step(self):
        Common(DUT).lockScreen()
        USB.disconnectUsb()
        PM.powerMeasure(sample=CONST.POWER.sample, mTime=600, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()   
        
    def tearDown(self):
        Common(DUT).unlockScreen()
        Setting(DUT).switchWifi("关闭")
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
