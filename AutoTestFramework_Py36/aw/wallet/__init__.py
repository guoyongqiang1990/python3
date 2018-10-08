#-*- coding:utf-8 -*-
import os
from aw.common import Common 
from uiautomator import Device
from logger import Logger
import time
class Wallet(Common):
    def __init__(self, sn=None):
        global d
        d = Device(sn)
        self.sn = sn

    
    def launchWallet(self):
        self.startActivity("io.nebulas.wallet.android.test/io.nebulas.wallet.android.module.launch.LaunchActivity")
        self.wait(3)
        self.clickWhenExist(text="我已仔细阅读并同意以上用户隐私协议及服务条款")
        self.clickWhenExist(text="继续")

    def createWallet(self,checkIfWait="YES"):
        self.clickByText("我的")
        self.clickByText("钱包")
        self.clickByText("添加钱包", screeScroll=True)
        self.clickByText("立即创建")
        if checkIfWait == "YES":
            self.inputText("000000")
            self.clickByText("同意")
            self.clickByText("下一步")
            self.inputText("000000")
            self.clickByText("确认")

            for i in range(5):
                if d(text="创建成功").exists:
                    self.goBack(1)
                else:
                    time.sleep(2)
        else:
            self.screenShot()

    def changeTab(self,tab):
        dic_tab={
            "home":"首页",
            "me":"我的",
            "dapps":"应用中心"

        }
        self.clickByText(dic_tab[tab])


    def imporWalletByPK(self):
        self.clickByText("添加钱包", screeScroll=True)
        self.clickByText("立即导入")
        self.clickByText("私钥（不安全）")
        self.clickByText("请输入私钥")
        self.inputText("612e58f24af35d10a1e2a8cb462c363135fb75a41bde686fd4608743bfeb4abd", if_enter="1")
        self.goBack(1)
        self.clickByText("同意")
        self.clickByText("开始导入")
        self.inputText("000000")
        self.clickByText("同意")
        self.clickByText("下一步")
        self.inputText("000000")
        self.clickByText("确认")
        self.clickByText("好的，我知道了")

    def inputInformation(self,address,amount,meno,gas="default",tokenType="NAS"):
        self.setText("io.nebulas.wallet.android.test:id/toAddressET",address)
        if tokenType!="NAS":
            self.clickById("io.nebulas.wallet.android.test:id/layout_coin_info")
            self.clickByText(tokenType)
        if gas!="default":
            self.clickByText("调整")
            self.clickById("io.nebulas.wallet.android.test:id/gasSeekBar")
            self.clickByText("确定")
        self.setText("io.nebulas.wallet.android.test:id/amountET", amount)
        self.setText("io.nebulas.wallet.android.test:id/remarksET", meno)
        self.goBack(1)
        self.clickByText("确认")

    def chooseWallet(self, name):
        self.clickByText(name)
        self.clickByText("确认")
        self.inputText("000000")




