#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：
1,关闭wifi
2,关闭蓝牙
3,关闭GPS
4,关闭NFC
5,开启数据连接
测试步骤：
1.3分钟后测试待机电流3分钟
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
        Setting(DUT).switchAirplane("关闭")
        Setting(DUT).switchWifi("关闭")
        Setting(DUT).switchBT("关闭")
        Setting(DUT).switchGPS("关闭")
        Setting(DUT).switchData("开启")
        Common(DUT).goBackHome()
        Common(DUT).clearRecentApp()
#         Common(DUT).clearUserData("com.gionee.softmanager")
    def test_step(self):
        Common(DUT).lockScreen()
        USB.disconnectUsb()
        PM.powerMeasure(sample=CONST.POWER.sample, mTime=1, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()   
        Common(DUT).unlockScreen()
        
    def tearDown(self):
#         Setting(DUT).switchData("关闭")
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
