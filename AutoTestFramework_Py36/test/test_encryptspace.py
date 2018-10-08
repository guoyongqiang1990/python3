#-*- coding:utf-8 -*-
'''
1，手机回到桌面，判断当前私密空间图标是否存在
2，进入私密空间，->高级设置，点击隐藏私密空间桌面图标，返回桌面
3，判断私密空间可见状态
'''
from aw import * 

class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
     
    def test_step(self):
        for i in range(LOOP.loop1):
            status1=Checkpoint(DUT).checkIfTextExistBySwipe("检查",text="私密空间", direction="left_right")
    #         Common(DUT).clickByText("私密空间",screeScroll=True,direction="left_right")
            Common(DUT).startActivity("com.gionee.encryptspace/.VerifyDialCodeActivity")
            Device(DUT)(resourceId="com.gionee.encryptspace:id/keyboard_value_number_sign").click()
            Device(DUT)(resourceId="com.gionee.encryptspace:id/keyboard_value_1").click()
            Device(DUT)(resourceId="com.gionee.encryptspace:id/keyboard_value_2").click()
            Device(DUT)(resourceId="com.gionee.encryptspace:id/keyboard_value_3").click()
            Device(DUT)(resourceId="com.gionee.encryptspace:id/keyboard_value_4").click()
            Device(DUT)(resourceId="com.gionee.encryptspace:id/keyboard_value_number_sign").click()
            Common(DUT).clickByText("高级设置")
            Common(DUT).clickByText("隐藏私密空间桌面图标")
            Common(DUT).goBack(2)
            Common(DUT).goHome()
            status2=Checkpoint(DUT).checkIfTextExistBySwipe("检查",text="私密空间", direction="left_right")
            self.assertEqual(status1, not status2, "失败")
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