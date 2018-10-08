#-*- coding:utf-8 -*-
'''
用例标题：
测试步骤：
1.进入相机
2.每10秒拍照一次
3.重复步骤2、3，执行80次
4.返回待机
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
        Common(DUT).clearRecentApp()
         
    def test_step(self):
        Common(DUT).startActivity("com.tencent.mobileqq/.activity.SplashActivity")
        Common(DUT).clickById("com.tencent.mobileqq:id/icon", 0)
        if not Common(DUT).exists(text="按住说话"):
            Common(DUT).click(82, 1852)
 
        Common(DUT).nohupTest("PowerTestCases.jar", "testQQ")
        USB.disconnectUsb()
        PM.powerMeasure(sample=100, mTime=900, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    

    def tearDown(self):
        Common(DUT).wait(10)
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
