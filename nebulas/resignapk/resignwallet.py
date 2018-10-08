# encoding: utf-8
import shutil
import os
import sys
#设置签名信息
#keystore_path = sys.argv[1]
keystore_path = "C:\\Users\\郭永强\\Desktop\\Nasnano2.2\\android.keystore"
keystore_pass = "123456"
keystore_split = keystore_path.split(os.sep)
keystore_alias = keystore_split[-1]
#keystore_alias = "android.keystore"
keystore_alias_pass = "123456"

#传入apk路径
root = os.getcwd()
#apk_path = sys.argv[2]
apk_path = "C:\\Users\\郭永强\\Desktop\\Nasnano2.2\\wallet.apk"
tmp_path = root + os.sep + "tmp"
path_split = apk_path.split(os.sep)
apk_name = path_split[-1]

#copy文件至tmp
if not os.path.exists(tmp_path):
	os.mkdir("tmp")
shutil.copyfile(apk_path,tmp_path+os.sep+apk_name)

# 删除签名信息
os.system("zip -d "+tmp_path+os.sep+apk_name+" META-INF/*")

#签名
os.chdir(tmp_path)
os.system("jarsigner -verbose -digestalg SHA1 -sigalg MD5withRSA -keystore "+ keystore_path + " -storepass " +keystore_pass + " -signedjar " +" wallet-sign.apk" +" wallet.apk " + keystore_alias +" -keypass " + keystore_alias_pass)
#验证签名
#os.system("jarsigner -verify -certs wallet-sign.apk")
os.chdir(root)

print ("证书更换完毕")
