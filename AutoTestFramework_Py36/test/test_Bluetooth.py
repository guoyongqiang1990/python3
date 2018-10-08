#-*- coding:utf-8 -*-
'''
1，手机返回桌面
2，点击进入设置，蓝牙
3,打开蓝牙开关
4，检测是否搜索到指定蓝牙设备
'''
from aw import * 

######################################
BTName= "GIONEE GN8003"              
TAG=__file__.split("\\")[-1]         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
        Common(DUT).putSettings("system","screen_off_timeout","1800000")
    def test_step(self):
        for i in range(LOOP.loop1):
            Common(DUT).clickByText("设置",screeScroll=True,direction="left_right")
    #         Common(DUT).launchSettings()
            Common(DUT).clickByText("蓝牙")
            Common(DUT).clickById("com.gionee.bluetooth:id/switch_widget")
            Common(DUT).switchWidget("false", "com.gionee.bluetooth:id/switch_widget")
            Common(DUT).wait(5)
        
            Checkpoint(DUT).checkIfExist("检查目标蓝牙是否存在",text=BTName)
            Common(DUT).goBack(2)
            Common(DUT).goHome()
    def tearDown(self):
        Common(DUT).clearRecentApp()

if __name__ == "__main__":
    unittest.main()
