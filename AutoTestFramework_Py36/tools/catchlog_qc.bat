@echo off

set sn=%1
set save_path=%2

if "%sn%"=="None" (
adb shell screencap -p /data/local/tmp/screenshot.png

adb pull /data/local/tmp/screenshot.png %save_path%/screenshot.png

adb shell rm /data/local/tmp/screenshot.png

adb pull data/misc/SelfHost/QCLogs %save_path%/QCLogs

::@echo "抓出GNlog"
adb pull /sdcard/GNLogs %save_path%/GNLogs

::@echo "抓出wlan log"
adb pull /sdcard/wlan_logs %save_path%/wlan_logs

::@echo "抓出trace"
adb pull /data/anr %save_path%/anr

::@echo "抓出tombstones"
adb pull /data/tombstones %save_path%/tombstones

::@echo "抓出last_kmsg"
adb shell cat /proc/last_kmsg > %save_path%/last_kmsg

::@echo "抓出recovery log"
adb pull /data/misc/gionee/recovery/ %save_path%//recovery

::@echo "抓出crash"
adb shell dumpsys dropbox system_app_crash --print>>%save_path%/Crash.txt

::@echo “抓出手机状态”
adb shell ps > %save_path%/ps.txt
adb shell dumpstate > %save_path%/dumpstate.txt
adb shell dumpsys > %save_path%/dumpsys.txt
adb shell top -t -d 2 -n 5 > %save_path%/top.txt
adb shell service list  > %save_path%/serviceList.txt

::@echo “抓出功耗RPM”
adb shell "cat /sys/kernel/debug/rpm_stats" > %save_path%/rpm.txt

) else (
adb -s %sn% shell screencap -p /data/local/tmp/screenshot.png

adb -s %sn% pull /data/local/tmp/screenshot.png %save_path%/screenshot.png

adb -s %sn% shell rm /data/local/tmp/screenshot.png

adb -s %sn% pull data/misc/SelfHost/QCLogs %save_path%/QCLogs

::@echo "抓出GNlog"
adb -s %sn% pull /sdcard/GNLogs %save_path%/GNLogs

::@echo "抓出wlan log"
adb -s %sn% pull /sdcard/wlan_logs %save_path%/wlan_logs

::@echo "抓出trace"
adb -s %sn% pull /data/anr %save_path%/anr

::@echo "抓出tombstones"
adb -s %sn% pull /data/tombstones %save_path%/tombstones

::@echo "抓出last_kmsg"
adb -s %sn% shell cat /proc/last_kmsg > %save_path%/last_kmsg

::@echo "抓出recovery log"
adb -s %sn% pull /data/misc/gionee/recovery/ %save_path%//recovery

::@echo "抓出crash"
adb -s %sn% shell dumpsys dropbox system_app_crash --print>>%save_path%/Crash.txt

::@echo “抓出手机状态”
adb -s %sn% shell ps > %save_path%/ps.txt
adb -s %sn% shell dumpstate > %save_path%/dumpstate.txt
adb -s %sn% shell dumpsys > %save_path%/dumpsys.txt
adb -s %sn% shell top -t -d 2 -n 5 > %save_path%/top.txt
adb -s %sn% shell service list  > %save_path%/serviceList.txt

::@echo “抓出功耗RPM”
adb -s %sn% shell "cat /sys/kernel/debug/rpm_stats" > %save_path%/rpm.txt

)
exit




