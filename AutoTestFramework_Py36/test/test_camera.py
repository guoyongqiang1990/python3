#-*- coding:utf-8 -*-
'''
1，手机回到桌面
2，点击进入相机应用
3,主摄像头开启闪关灯拍照
4，切换前摄拍照
5，重复3,4操作
'''
from aw import * 
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
        Common(DUT).putSettings("system","screen_off_timeout","1800000")
        Common(DUT).clickByText("相机",screeScroll=True,direction="left_right")
        if Device(DUT)(className="android.widget.Button").exists:
            Device(DUT)(className="android.widget.Button").click()
            Device(DUT)(text="继续").click()

    def test_step(self):
        for i in range(LOOP.loop1):
            Common(DUT).clickById("com.android.camera:id/flashlight_picker")
            Device(DUT)(text="打开").click()
            Common(DUT).clickById("com.android.camera:id/shutter_button_icon")
            time.sleep(3)
            Common(DUT).clickById("com.android.camera:id/camera_picker")
            time.sleep(2)
            Common(DUT).clickById("com.android.camera:id/shutter_button_icon")
            time.sleep(2)
            Common(DUT).clickById("com.android.camera:id/camera_picker")
        
        
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