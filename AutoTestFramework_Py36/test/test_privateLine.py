#-*- coding:utf-8 -*-
'''
1,手机回到桌面
2，点击专线通话进入应用
3，若没有帐号，登入帐号
4，判断正常进入应用
'''
from aw import * 

phoneNum="13810869420"
class TestScript(unittest.TestCase):
    
    def setUp(self):
        Common(DUT).goHome()
        Common(DUT).putSettings("system","screen_off_timeout","18000000")
    def test_step(self):
        for i in range(LOOP.loop1):
            Common(DUT).clickByText("专线通话",screeScroll=True,direction="left_right")
            if Device(DUT)(resourceId="com.gionee.im:id/phone_number").exists:
                Common(DUT).clickWhenExist(resourceId="com.gionee.im:id/phone_number")
                Device(DUT)(resourceId="com.gionee.im:id/phone_number").set_text(phoneNum)
                Common(DUT).clickWhenExist(text="获取验证码")
                Common(DUT).wait(10)
                Common(DUT).clickWhenExist(text="激活")
            Common(DUT).wait(2)
            Checkpoint(DUT).checkIfExist("检查专线通话打开", resourceId="com.gionee.im:id/empty")
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