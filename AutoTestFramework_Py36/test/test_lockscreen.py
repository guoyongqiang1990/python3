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

    def test_step(self):
        for i in range(LOOP.loop1):
            Common(DUT).lockScreen()
            Device(DUT).wakeup()
            Device(DUT).swipe(350, 852, 350, 301, 5)#解锁
            time.sleep(0.2)
            Checkpoint(DUT).checkIfExist("message",className="android.view.ViewGroup")
        
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