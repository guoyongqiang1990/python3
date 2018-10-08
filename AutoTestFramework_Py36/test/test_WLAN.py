#-*- coding:utf-8 -*-
'''
1，手机返回桌面
2，点击进入设置，WLAN
3,打开WiFi开关
4，检测是否搜索到指定热点

'''
from aw import * 
wifiName= "Google"
class TestScript(unittest.TestCase):

    def setUp(self):
        Common(DUT).goHome()
        Common(DUT).putSettings("system","screen_off_timeout","18000000")
    def test_step(self):
        for i in range(LOOP.loop1):
            Common(DUT).clickByText("设置",screeScroll=True,direction="left_right")
    #         Common(DUT).launchSettings()
            Common(DUT).clickByText("WLAN")
            Common(DUT).clickById("com.gionee.setting.adapter.wifi:id/switch_widget")
            Common(DUT).switchWidget("false", "com.gionee.setting.adapter.wifi:id/switch_widget")
            Common(DUT).wait(5)
            Checkpoint(DUT).checkIfExist("检查目标wifi是否存在",text=wifiName)
            Common(DUT).goBack(2)
            Common(DUT).goHome()
    def tearDown(self):
        Common(DUT).clearRecentApp()
        
if __name__ == "__main__":
#     unittest.main()

    name=__file__.split("\\")[-1]
    name=name.split('.')[0]
    record=time.strftime("%Y-%m-%d_%H-%M-%S")
    testsuite=unittest.TestSuite()
    testsuite.addTest(TestScript("test_step"))
    filename=sys.path[1]+"\\report\\"+name+record+".html"
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=name,description='Test_Report')
    runner.run(testsuite)