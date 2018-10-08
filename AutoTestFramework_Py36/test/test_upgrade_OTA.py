#-*- coding:utf-8 -*-
'''
1，手机返回桌面
2，点击进入设置，蓝牙
3,打开蓝牙开关
4，检测是否搜索到指定蓝牙设备
'''
from aw import * 

######################################              
TAG=__file__.split("\\")[-1]         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
        Common(DUT).putSettings("system","screen_off_timeout","1800000")
    def test_step(self):
        Common(DUT).upgradeByOTA(r"Z:\git_release\2017-03\02_ANDROID\G1602A\G1602A-T0104-170329AA_user\BJ_G1602A_T0104_OTA\ota\BJ_G1602A_update_amigo3.5.0_T0104.zip")

if __name__ == "__main__":
    unittest.main()
