#-*- coding:utf-8 -*-
from aw import *
'''
用例标题:nebpay API Normal
测试步骤：
1.创建5个钱包
'''

######################################             
TAG=__file__.split("\\")[-1]         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
        Common(DUT).clearUserData("io.nebulas.wallet.android.test")

    def test_step(self):
        Wallet(DUT).launchWallet()
        for i in range(1,51):
            Wallet(DUT).createWallet()
            result = Checkpoint(DUT).checkIfExist("检测；钱包是否创建成功", text="钱包 "+str(i))
            self.assertEqual(result, True)
        Wallet(DUT).createWallet(checkIfWait="NO")
    def tearDown(self):
        Common(DUT).goBack(4)
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
