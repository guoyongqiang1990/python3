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
        Common(DUT).pushFile("video\\powerConsumption720P_11.25.mp4", "/storage/sdcard0/")
        Common(DUT).adbCmd("install -r -d "+ resourcePath+"apk\\Amigo_Video_6.0-local.apk")
        
    def test_step(self):
        Common(DUT).startActivity("com.gionee.video/.VideoMainActivity")
        Common(DUT).clickWhenExist(text="继续")
#         Common(DUT).goBack()
        Common(DUT).clickByText("扫描")
        Common(DUT).nohupTest("PowerTestCases.jar", "testVideo")
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=180, caseName=TAG)
        PM.powerMeasure(sample=100, mTime=600, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
 
    def tearDown(self):
        Common(DUT).wait(10)
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
