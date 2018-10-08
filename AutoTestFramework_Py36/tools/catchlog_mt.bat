@echo off

set sn=%1
set save_path=%2

if "%sn%"=="None" (
adb shell screencap -p /data/local/tmp/screenshot.png

adb pull /data/local/tmp/screenshot.png %save_path%/screenshot.png

adb shell rm /data/local/tmp/screenshot.png

::3.  开始抓取内核进程列表
adb shell ps > %save_path%/ps

::4.  开始抓取CPU信息
adb shell dumpsys cpuinfo > %save_path%/dump_cpuinfo

::5.  开始抓取内存信息
adb shell dumpsys meminfo > %save_path%/dump_meminfo

::6.  开始抓取电量信息
adb shell dumpsys battery > %save_path%/dump_battery

::7.  开始抓取mobilelog & aee_exp & anr
adb pull /mnt/sdcard/mtklog/mobilelog %save_path%/mtklog/mobilelog
adb pull /mnt/sdcard2/mtklog/mobilelog %save_path%/mtklog/mobilelog

adb pull /mnt/sdcard/mtklog/aee_exp %save_path%/mtklog/aee_exp
adb pull /mnt/sdcard2/mtklog/aee_exp %save_path%/mtklog/aee_exp

adb pull /mnt/sdcard/mtklog/anr %save_path%/mtklog/anr
adb pull /mnt/sdcard2/mtklog/anr %save_path%/mtklog/anr

::8.  开始抓取ANR信息
adb pull /data/anr %save_path%/anr

::9.  开始抓取db信息
adb pull /data/aee_exp %save_path%/data_aee_exp

::10.  开始抓取存储器分区信息
adb shell df > %save_path%/df

::11. 开始抓取特殊信息
adb pull /data/mobilelog %save_path%/data_mobilelog
adb pull /data/core %save_path%/data_core
adb pull /data/tombstones %save_path%/tombstones

::12. 开始抓取全部安装包信息
cd %save_path%
mkdir packageInfo
cd ..
adb shell pm list package > %save_path%/packageInfo/packageList
adb shell pm list package -f > %save_path%/packageInfo/packageDirList
adb shell pm list package -d > %save_path%/packageInfo/disabledPackageList
adb shell pm list package -s > %save_path%/packageInfo/systemPackageList
adb shell pm list package -3 > %save_path%/packageInfo/thirdPackageList
adb shell pm get-install-location >> %save_path%/packageInfo/otherInfo
adb shell pm list users >> %save_path%/packageInfo/otherInfo

) else (
adb -s %sn% shell screencap -p /data/local/tmp/screenshot.png

adb -s %sn% pull /data/local/tmp/screenshot.png %save_path%/screenshot.png

adb -s %sn% shell rm /data/local/tmp/screenshot.png

::3.  开始抓取内核进程列表
adb -s %sn% shell ps > %save_path%/ps

::4.  开始抓取CPU信息
adb -s %sn% shell dumpsys cpuinfo > %save_path%/dump_cpuinfo

::5.  开始抓取内存信息
adb -s %sn% shell dumpsys meminfo > %save_path%/dump_meminfo

::6.  开始抓取电量信息
adb -s %sn% shell dumpsys battery > %save_path%/dump_battery

::7.  开始抓取mobilelog & aee_exp & anr
adb -s %sn% pull /mnt/sdcard/mtklog/mobilelog %save_path%/mtklog/mobilelog
adb -s %sn% pull /mnt/sdcard2/mtklog/mobilelog %save_path%/mtklog/mobilelog

adb -s %sn% pull /mnt/sdcard/mtklog/aee_exp %save_path%/mtklog/aee_exp
adb -s %sn% pull /mnt/sdcard2/mtklog/aee_exp %save_path%/mtklog/aee_exp

adb -s %sn% pull /mnt/sdcard/mtklog/anr %save_path%/mtklog/anr
adb -s %sn% pull /mnt/sdcard2/mtklog/anr %save_path%/mtklog/anr

::8.  开始抓取ANR信息
adb -s %sn% pull /data/anr %save_path%/anr

::9.  开始抓取db信息
adb -s %sn% pull /data/aee_exp %save_path%/data_aee_exp

::10.  开始抓取存储器分区信息
adb -s %sn% shell df > %save_path%/df

::11. 开始抓取特殊信息
adb -s %sn% pull /data/mobilelog %save_path%/data_mobilelog
adb -s %sn% pull /data/core %save_path%/data_core
adb -s %sn% pull /data/tombstones %save_path%/tombstones

::12. 开始抓取全部安装包信息
cd %save_path%
mkdir packageInfo
cd ..
adb -s %sn% shell pm list package > %save_path%/packageInfo/packageList
adb -s %sn% shell pm list package -f > %save_path%/packageInfo/packageDirList
adb -s %sn% shell pm list package -d > %save_path%/packageInfo/disabledPackageList
adb -s %sn% shell pm list package -s > %save_path%/packageInfo/systemPackageList
adb -s %sn% shell pm list package -3 > %save_path%/packageInfo/thirdPackageList
adb -s %sn% shell pm get-install-location >> %save_path%/packageInfo/otherInfo
adb -s %sn% shell pm list users >> %save_path%/packageInfo/otherInfo
)
exit

