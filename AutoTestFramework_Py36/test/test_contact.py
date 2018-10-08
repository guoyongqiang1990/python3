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
            Common(DUT).shell("reboot")
            time.sleep(120)
            Device(DUT).wakeup()
            Device(DUT).swipe(350, 852, 350, 301, 5)#解锁
            Common(DUT).clickByText("联系人", screeScroll=True,direction="left_right")
            Common(DUT).clickByText("更多")
            Common(DUT).clickByText("批量操作")
            Common(DUT).clickByText("全部选择")
            Checkpoint(DUT).checkIfExist("检查联系人数量",text = "已选中2个")
        
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