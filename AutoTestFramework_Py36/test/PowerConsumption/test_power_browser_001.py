#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：移动数据开启
测试步骤：
1.从桌面icon进入浏览器，浏览网页；
2.back键退出,返回桌面，锁屏后，等待3分钟
3.测试待机电流5分钟
预期结果：

'''
from aw import *
from aw.power import USB,PM 
######################################             
TAG=__file__.split("\\")[-1]
fPath=rootPath+"\\"+TAG          
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Setting(DUT).switchData("开启")
        Common(DUT).clearRecentApp()
        Common(DUT).clearUserData("com.android.browser")
    def test_step(self):
        Common(DUT).startActivity("com.android.browser/.BrowserActivity")
        Common(DUT).clickWhenExist(text="继续")
        Common(DUT).clickByText("百度")
        Common(DUT).click(111,555)
        for i in range(5):
            Common(DUT).swipe(540, 1484, 540, 580, 40) 
            Common(DUT).clickWhenExist(text="共享位置")
            time.sleep(1)
        Common(DUT).goBack(2)
        Common(DUT).clickByText("退出")
#         result = Checkpoint(DUT).checkIfExist("检测点1",text="日历") 
#         self.assertEqual(result, True)
        Common(DUT).lockScreen()
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()  
        Common(DUT).unlockScreen()
    def tearDown(self):
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
