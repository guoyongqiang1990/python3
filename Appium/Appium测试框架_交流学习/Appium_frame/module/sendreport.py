# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : Data.py
# @Software: PyCharm
# @Version ：V1.0
import time, os, smtplib
import mimetypes, zipfile
import email.mime.multipart, email.mime.text, email.mime.base

#获取当前系统时间，生成HTML路径，生成IMG路径
def time_fixed():
	time_fixed = '%s'%(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
	img_file = (os.getcwd() + '/all_script/Report/img_result/' + time_fixed)
	file_name = (os.getcwd() + '/all_script/Report/html_result/')+ time_fixed + '测试报告详情.html'
	return  time_fixed, img_file, file_name

#取得定义的上面生成信息
gain_time = time_fixed()[0]
img_file = time_fixed()[1]
file_name = time_fixed()[2]

#压缩文件
def zip(path, path_new):
	try:
		import zlib
		compression = zipfile.ZIP_DEFLATED
	except:
		compression = zipfile.ZIP_STORED
	start = path.rfind(os.sep) + 1
	filename = path_new + gain_time + '运行过程截图.zip'  #压缩后的文件名
	z = zipfile.ZipFile(filename,mode = "w",compression = compression)
	try:
		for dirpath,dirs,files in os.walk(path):
			for file in files:
				if file == filename or file == "zip.py":
					continue
				# print(file)
				z_path = os.path.join(dirpath,file)
				z.write(z_path,z_path[start:])
		z.close()
	except:
		if z:
			z.close()

#邮件收发
def send_mail(file_names):

	# 构造MIMEMultipart对象做为根容器  
	main_msg = email.mime.multipart.MIMEMultipart()
	now_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))

	# 设置根容器属性 (阿里邮箱正常使用)
	From = 'XXX@XXX.com'   #发送邮箱
	To = "XXX@XXX.com"  #收件邮箱
	main_msg['From'] = From
	main_msg['To'] = To
	subject = "自动化测试报告"+time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
	main_msg['Subject'] = subject
	server = smtplib.SMTP_SSL("smtp.mxhichina.com",465)
	server.login("登陆邮箱用户名", "登陆邮箱密码") #(发送邮箱登陆的用户名与密码)

	# 构造MIMEText对象做为邮件显示内容并附加到根容器  
	#定义正文
	mail_body = 'HI, ALL:   这是  ' + now_time +  '  结束的测试报告，请您查收。具体内容请参见附件。'
	text_msg= email.mime.text.MIMEText(mail_body, _subtype='html', _charset='utf-8')
	main_msg.attach(text_msg)   

	for file_name in file_names: 
		# 读入文件内容并格式化
		data = open(file_name, 'rb')  
		ctype,encoding = mimetypes.guess_type(file_name)  
		if ctype is None or encoding is not None:
			ctype = 'application/octet-stream'
		maintype,subtype = ctype.split('/',1)  
		file_msg = email.mime.base.MIMEBase(maintype, subtype)
		file_msg.set_payload(data.read())
		data.close()
		email.encoders.encode_base64(file_msg)  #把附件编码

		# 设置附件头  
		basename = os.path.basename(file_name)  
		file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头  
		main_msg.attach(file_msg)  

		# 得到格式化后的完整文本  
		fullText = main_msg.as_string()

		# 用smtp发送邮件 
	# server.sendmail(From, ["wei_shen@dingyuegroup.cn", "my126sw@126.com"], fullText)  #添加抄送
	server.sendmail(From, To, fullText)  #不添加抄送

#查找测试报告，调用发邮件功能
def sendreport():
	#找到最新html的文件
	new_files = []
	result_html = (os.getcwd() + '/all_script/Report/html_result/')
	lists  = os.listdir(result_html)
	lists.sort(key = lambda fn: os.path.getmtime(result_html+ '/'+ fn )
		if not os.path.isdir(result_html+ '/'+ fn ) else 0)
	print(u'最新测试生成的报告:'+ lists[-1])
	new_file = os.path.join(result_html, lists[-1])
	new_files.append(new_file)

	#找到最新text的文件
	result_dir = (os.getcwd() + '/all_script/Report/text_result/')
	lists  = os.listdir(result_dir)
	lists.sort(key = lambda fn: os.path.getmtime(result_dir+ '/'+ fn )
		if not os.path.isdir(result_dir+ '/'+ fn ) else 0)
	print(u'最新测试生成的报告:'+ lists[-1])
	new_file = os.path.join(result_dir, lists[-1])
	new_files.append(new_file)

	#找到最新的zip文件
	zip_result_img = (os.getcwd() + '/all_script/Report/img_result/' + gain_time + '/')
	path_new = (os.getcwd() + '/all_script/Report/img_result/')
	zip(zip_result_img, path_new)
	result_img = (os.getcwd() + '/all_script/Report/img_result/')
	lists  = os.listdir(result_img)
	lists.sort(key = lambda fn: os.path.getmtime(result_img+ '/'+ fn )
		if not os.path.isdir(result_img+ '/'+ fn ) else 0)
	print(u'最新测试生成的报告:'+ lists[-1])
	new_file = os.path.join(result_img, lists[-1])
	new_files.append(new_file)
	print (new_files)
	
	#调用发邮件模块
	send_mail(new_files)