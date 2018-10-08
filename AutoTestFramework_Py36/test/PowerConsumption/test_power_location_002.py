#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：GPS开启
测试步骤：
1.打开高德地图，进入地图首页
2.刷新地理位置后，back回到桌面，3分钟后测试待机3分钟
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
        Setting(DUT).switchGPS("开启")
        Setting(DUT).switchData("开启")
        Common(DUT).clearRecentApp()
#         Common(DUT).clearUserData("com.gionee.softmanager")
    def test_step(self):
        Common(DUT).startActivity("com.autonavi.minimap/com.autonavi.map.activity.NewMapActivity")
        Common(DUT).clickWhenExist(text="进入地图")
        Common(DUT).clickWhenExist(text="忽略")
        Common(DUT).clickById("com.autonavi.minimap:id/GpsButton")
        Common(DUT).wait(3)
        Common(DUT).goBackHome()
        Common(DUT).lockScreen()
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=CONST.POWER.sample, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()   
        Common(DUT).unlockScreen()
        
    def tearDown(self):
        Setting(DUT).switchGPS("关闭")
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
