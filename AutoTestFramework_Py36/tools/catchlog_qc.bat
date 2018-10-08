@echo off

set sn=%1
set save_path=%2

if "%sn%"=="None" (
adb shell screencap -p /data/local/tmp/screenshot.png

adb pull /data/local/tmp/screenshot.png %save_path%/screenshot.png

adb shell rm /data/local/tmp/screenshot.png

adb pull data/misc/SelfHost/QCLogs %save_path%/QCLogs

::@echo "ץ��GNlog"
adb pull /sdcard/GNLogs %save_path%/GNLogs

::@echo "ץ��wlan log"
adb pull /sdcard/wlan_logs %save_path%/wlan_logs

::@echo "ץ��trace"
adb pull /data/anr %save_path%/anr

::@echo "ץ��tombstones"
adb pull /data/tombstones %save_path%/tombstones

::@echo "ץ��last_kmsg"
adb shell cat /proc/last_kmsg > %save_path%/last_kmsg

::@echo "ץ��recovery log"
adb pull /data/misc/gionee/recovery/ %save_path%//recovery

::@echo "ץ��crash"
adb shell dumpsys dropbox system_app_crash --print>>%save_path%/Crash.txt

::@echo ��ץ���ֻ�״̬��
adb shell ps > %save_path%/ps.txt
adb shell dumpstate > %save_path%/dumpstate.txt
adb shell dumpsys > %save_path%/dumpsys.txt
adb shell top -t -d 2 -n 5 > %save_path%/top.txt
adb shell service list  > %save_path%/serviceList.txt

::@echo ��ץ������RPM��
adb shell "cat /sys/kernel/debug/rpm_stats" > %save_path%/rpm.txt

) else (
adb -s %sn% shell screencap -p /data/local/tmp/screenshot.png

adb -s %sn% pull /data/local/tmp/screenshot.png %save_path%/screenshot.png

adb -s %sn% shell rm /data/local/tmp/screenshot.png

adb -s %sn% pull data/misc/SelfHost/QCLogs %save_path%/QCLogs

::@echo "ץ��GNlog"
adb -s %sn% pull /sdcard/GNLogs %save_path%/GNLogs

::@echo "ץ��wlan log"
adb -s %sn% pull /sdcard/wlan_logs %save_path%/wlan_logs

::@echo "ץ��trace"
adb -s %sn% pull /data/anr %save_path%/anr

::@echo "ץ��tombstones"
adb -s %sn% pull /data/tombstones %save_path%/tombstones

::@echo "ץ��last_kmsg"
adb -s %sn% shell cat /proc/last_kmsg > %save_path%/last_kmsg

::@echo "ץ��recovery log"
adb -s %sn% pull /data/misc/gionee/recovery/ %save_path%//recovery

::@echo "ץ��crash"
adb -s %sn% shell dumpsys dropbox system_app_crash --print>>%save_path%/Crash.txt

::@echo ��ץ���ֻ�״̬��
adb -s %sn% shell ps > %save_path%/ps.txt
adb -s %sn% shell dumpstate > %save_path%/dumpstate.txt
adb -s %sn% shell dumpsys > %save_path%/dumpsys.txt
adb -s %sn% shell top -t -d 2 -n 5 > %save_path%/top.txt
adb -s %sn% shell service list  > %save_path%/serviceList.txt

::@echo ��ץ������RPM��
adb -s %sn% shell "cat /sys/kernel/debug/rpm_stats" > %save_path%/rpm.txt

)
exit




