# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:23:29 2019

"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

#发送邮箱服务
smtpsever = 'smtp.qq.com'
user = 'xxxxxx@qq.com'
password = 'xxxxxxxxxx'

#发送邮箱,接收邮箱
sender = 'xxxxxxxxx@qq.com'
receiver = 'xxxxxxx@163.com'

#主题
subject = 'python eamil test'

#编写HTML类型的正文邮件
'''
msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = Header(subject, 'utf-8')
'''

#添加附件
sendfile = open('log.txt', 'rb').read()
att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="log.txt"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot['From'] = sender
msgRoot['To'] = sender
msgRoot.attach(MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8'))       
msgRoot.attach(att) 
             
#连接发送邮件
try:
    smtp = smtplib.SMTP_SSL(smtpsever, 465)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    print("Success!")
except smtplib.SMTPException as e: 
    print ("Falied,%s" %e) 


