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
        Wallet(DUT).launchWallet()
        Wallet(DUT).imporWalletByPK()
    def test_step(self):
        Wallet(DUT).changeTab("home")
        Common(DUT).clickByText("转账")
        Wallet(DUT).inputInformation("n1JEBqmiMeVyiD6a5Qsa6eFktWV2UAFkyZz","0.000000000000000001","大大的世界","middle","NAS")
        Wallet(DUT).chooseWallet("钱包 1")
        Common(DUT).wait(3)
        result = Checkpoint(DUT).checkIfExist("检测；转账数量是否正确", text="-0.000000000000000001NAS")
        self.assertEqual(result, True)
        result = Checkpoint(DUT).checkIfExist("检测；发款方正确", text="n1awhGQjpjWya785r5ht7FYTNoVAmQAqKpb")
        self.assertEqual(result, True)
        result = Checkpoint(DUT).checkIfExist("检测；收款方正确", text="n1JEBqmiMeVyiD6a5Qsa6eFktWV2UAFkyZz")
        self.assertEqual(result, True)

        Common(DUT).wait(45)
        result = Checkpoint(DUT).checkIfNotExist("检测点3:交易状态", text="(0/15)")
        self.assertEqual(result, True)
        Common(DUT).goBack()
        Common(DUT).clickByText("转账")
        Wallet(DUT).inputInformation("n1JEBqmiMeVyiD6a5Qsa6eFktWV2UAFkyZz", "0.000000000000000001", "大大的世界","middle", "ATP")
        Wallet(DUT).chooseWallet("钱包 1")
        Common(DUT).wait(3)
        result = Checkpoint(DUT).checkIfExist("检测；转账数量是否正确", text="-0.000000000000000001ATP")
        self.assertEqual(result, True)
        result = Checkpoint(DUT).checkIfExist("检测；发款方正确", text="n1awhGQjpjWya785r5ht7FYTNoVAmQAqKpb")
        self.assertEqual(result, True)
        result = Checkpoint(DUT).checkIfExist("检测；收款方正确", text="n1JEBqmiMeVyiD6a5Qsa6eFktWV2UAFkyZz")
        self.assertEqual(result, True)
        result = Checkpoint(DUT).checkIfExist("检测；备注", text="大大的世界")
        self.assertEqual(result, True)
        Common(DUT).wait(45)
        result = Checkpoint(DUT).checkIfNotExist("检测点3:交易状态", text="(0/15)")
        self.assertEqual(result, True)

    def tearDown(self):
        return True

if __name__ == "__main__":
    unittest.main()
