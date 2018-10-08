#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：锁屏后自动清理开启
测试步骤：
1.普通模式，锁屏15分钟后测试待机电流
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
        Common(DUT).clearRecentApp()
        Common(DUT).clearUserData("com.gionee.softmanager")
    def test_step(self):
        Common(DUT).startActivity("com.gionee.softmanager/.MainActivity")
        Common(DUT).clickById("com.gionee.softmanager:id/img_actionbar_custom")
        Common(DUT).switchWighetByIndex("开启", 6)
        Common(DUT).goBack()
        Common(DUT).clickByText("省电管理")
        Common(DUT).clickByText("普通模式")
        Common(DUT).lockScreen()
        Common(DUT).wait(5)
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()   
        Common(DUT).unlockScreen()
        
    def tearDown(self):
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
