# encoding: utf-8
import shutil
import os
import sys
#设置签名信息
keystore_path = "C:\\Users\\郭永强\\Desktop\\Nasnano2.2"
keystore_pass = "123456"
keystore_alias = "android.keystore"
keystore_alias_pass = "123456"
#传入apk路径
root = os.getcwd()
tmp_path = root + os.sep + "tmp"
apk_path = sys.argv[1]
path_spilt = apk_path.split(os.sep)
# p_length = len(path_spilt)
# apk_name = path_spilt[p_length-1]
apk_name = path_spilt[-1]

#copy文件至tmp
if not os.path.exists(tmp_path):
	os.system("mkdir tmp")
shutil.copyfile(apk_path,tmp_path+apk_name)

# 删除签名信息
os.system("zip -d "+tmp_path+apk_name+" META-INF/*")

# 解压
os.system("unzip -d "+tmp_path+" "+tmp_path+apk_name)
# 删除原apk
if os.path.exists(tmp_path+apk_name):
	os.remove(tmp_path+apk_name)
# 更新资源
os.system("rsync -avz --progress --exclude .DS_Store "+root+"/res/ "+tmp_path+"/res")
# 打包
os.chdir(tmp_path)
os.system("zip -r "+root+"/release-nosign.apk "+"*")
os.chdir(root)
#签名
os.system("jarsigner -verbose -digestalg SHA1 -sigalg MD5withRSA -keystore "+ keystore_path + " -storepass " +keystore_pass + " -signedjar release-sign.apk release-nosign.apk " + keystore_alias +" -keypass " + keystore_alias_pass)
#压缩对齐
os.system("/Users/playcrab/zhangnan/adt-bundle-mac-x86_64-20140702/sdk/build-tools/24.0.1/zipalign -v 4 release-sign.apk release.apk")
#删除临时文件
shutil.rmtree(tmp_path)
#验证签名
os.system("jarsigner -verify -certs release.apk")
print ("APK资源更换完毕")
