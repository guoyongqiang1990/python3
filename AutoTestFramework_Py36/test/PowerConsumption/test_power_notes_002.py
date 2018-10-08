#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：飞行模式开启
测试步骤：
1，创建一个带文字、图片、语音、提醒的记事本
2，back键退出，等待提醒结束，3分钟后测试待机电流
预期结果：

'''
from aw import * 
from aw.power import USB,PM 
# from aw.power import Power,USB 
######################################             
TAG=__file__.split("\\")[-1]      
fPath=rootPath+"\\"+TAG         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Setting(DUT).switchAirplane("开启")
        Common(DUT).clearRecentApp()
        Common(DUT).clearUserData("com.gionee.note")
    def test_step(self):
        Common(DUT).startActivity("com.gionee.note/.HomeActivity")
        Common(DUT).clickByText("新建")
        #添加文本
        Common(DUT).inputText("I am testing!")
        #添加照片
        Common(DUT).clickById("com.gionee.note:id/action_camera")
        Common(DUT).clickWhenExist(text="继续")
        Common(DUT).clickById("com.android.camera:id/shutter_button_icon")
        Common(DUT).clickById("com.android.camera:id/review_btn_done")
        #添加录音
        Common(DUT).clickById("com.gionee.note:id/action_recorde")
        Common(DUT).wait(5)
        Common(DUT).clickById("com.gionee.note:id/sound_recorder_stop")
        #添加提醒
        Common(DUT).clickById("com.gionee.note:id/action_reminder")
        Common(DUT).clickById("com.gionee.note:id/reminder_time_text")
        Common(DUT).swipe(723, 1428, 723, 1300, 50)#适配G1602A坐标
        Common(DUT).clickByText("确定")
        Common(DUT).clickById("com.gionee.note:id/new_note_activity_title_layout_delete")
        Common(DUT).clickByText("加密")
        Common(DUT).goBackHome()
        Common(DUT).wait(60)
        Common(DUT).lockScreen()
        Common(DUT).wait(5)
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()   
        Common(DUT).unlockScreen()
        
    def tearDown(self):
        Setting(DUT).switchAirplane("关闭")

        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
