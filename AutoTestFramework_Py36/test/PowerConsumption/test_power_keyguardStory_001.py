#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：开启双击灭屏
测试步骤：
1.亮屏状态下双击灭屏，3分钟后测试待机电流
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
    def test_step(self):
        Common(DUT).startActivity("com.amigo.keyguard/com.amigo.navi.keyguard.category.CategoryBaseActivity")
        Common(DUT).clickById("com.amigo.keyguard:id/category_setting")
        
        Common(DUT).switchWidget("false", "com.amigo.keyguard:id/settings_switch_double_desktop_lock")
        Common(DUT).goBackHome()
        Common(DUT).lockScreen()
        Common(DUT).wakeUp()
        Common(DUT).doubleClick(500, 500)

        Common(DUT).wait(5)
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb() 
        Common(DUT).unlockScreen()
        Common(DUT).startActivity("com.amigo.keyguard/com.amigo.navi.keyguard.category.CategoryBaseActivity")
        Common(DUT).clickById("com.amigo.keyguard:id/category_setting")
        
        Common(DUT).switchWidget("true", "com.amigo.keyguard:id/settings_switch_double_desktop_lock")
        
    def tearDown(self):
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
