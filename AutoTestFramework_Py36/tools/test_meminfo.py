#-*- coding:utf-8 -*-
'''
1，开机获取 meminfo1
2，主菜单所有应用运行 monkey 5分钟
3,获取 meminfo2
4，一键清理后台 获取 meminfo3
5，灭屏待机10分钟，获取 meminfo4
'''
from aw import * 
app_dic={
    "相册":"com.gionee.gallery/everphoto.activity.GuestMainActivity",
    "音乐":"com.android.music/.MusicScanResultActivity",
    "相机":"com.android.camera/.CameraLauncher",
    "时钟":"com.android.deskclock/.AlarmClock",
    "日历":"com.android.calendar/.AllInOneActivity",
    "主题壁纸":"com.gionee.change/.activity.ChangeGridActivity",
    "系统管家":"com.gionee.softmanager/.MainActivity",
    "拨号":"com.android.contacts/.activities.DialtactsActivity",
    "信息":"com.android.mms/.ui.BootActivity",
    "浏览器":"com.android.browser/.GNBrowserActivity",
    "私密空间":"com.gionee.encryptspace/.VerifyDialCodeActivity",
    "购物大厅":"com.gionee.client/.GNSplashActivity",
    "软件商店":"com.gionee.aora.market/.GoApkLoginAndRegister",
    "微信":"com.tencent.mm/.ui.LauncherUI",
    "视频":"com.gionee.video/.VideoMainActivity",
    "游戏大厅":"gn.com.android.gamehall/gn.com.android.gamehall.GNMainActivity",
    "高德地图":"com.autonavi.minimap/com.autonavi.map.activity.SplashActivity",
    "阅读":"com.chaozh.iReaderGionee/com.chaozh.iReader.ui.activity.WelcomeActivity",
    "记事本":"com.gionee.note/.HomeActivity",
    "电子邮件":"com.android.email/com.kingsoft.email.activity.Welcome",
    "金立翻译":"com.iflytek.translate/com.iflytek.business.home.Home",
    "金立健康":"com.gionee.www.healthy/.launch.view.LaunchPageActivity",
    "天气":"com.coolwind.weather/.SplashActivity",
    "收音机":"com.ximalaya.ting.android.gionee/.activity.WelcomeActivity",
    "儿童模式":"com.gionee.kidshome/.IndexActivity",
    "计算器":"com.android.calculator2/.",
    "文件管理":"com.gionee.filemanager/.FileExplorerTabActivity",
    "下载管理":"com.android.providers.downloads/.DownloadProvider",
    "指南针":"jlzn.com.android.compass/.",
    "金立遥控":"com.kookong.app.gionee/com.hzy.tvmao.view.activity.AppStartActivity ",
    "文件快传":"com.gionee.wlandirect/.view.HomeActivity",
    "用户中心":"com.gionee.gnservice/.UserCenterActivity",
    "搜狗搜索":"com.sogou.activity.src/.SplashActivity",
    "爱奇艺":"com.qiyi.video/.WelcomeActivity",
    "今日头条":"com.ss.android.article.news/.activity.SplashActivity",
    "QQ浏览器":"com.tencent.mtt/.SplashActivity",
    "手机管家":"com.tencent.qqpimsecure/com.tencent.server.fore.QuickLoadActivity",
    "腾讯新闻":"com.tencent.news/.activity.SplashActivity",
    "手机京东":"com.jingdong.app.mall/.MainActivity",
    "美团":"com.sankuai.meituan/.activity.PreloadedWelcome",
    "JJ斗地主":"cn.jj/.mobile.lobby.view.Main",
    
    }
Common(DUT).shell("dumpsys meminfo >d:\meminfo1.txt")
 
for key in app_dic.keys():
    app = app_dic[key].split("/")[0]
    print app
    print time.strftime("%Y-%m-%d_%H-%M-%S")
    Common(DUT).shell("monkey -p "+app+" --throttle 500 -v 2000")
Common(DUT).wait(60)
Common(DUT).goHome()
Common(DUT).shell("dumpsys meminfo >d:\meminfo2.txt")
Common(DUT).wait(60)
Common(DUT).clearRecentApp()
Common(DUT).wait(5)
Common(DUT).shell("dumpsys meminfo >d:\meminfo3.txt")
Device(DUT).sleep()
Common(DUT).wait(600)
Common(DUT).shell("dumpsys meminfo >d:\meminfo4.txt")
 
print("finished")
