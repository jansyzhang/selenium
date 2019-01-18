# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:31:23 2019

"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

#发送邮件
def send_email(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    
    smtpsever = 'smtp.qq.com'
    user = 'xxxxxxx@qq.com'
    password = 'xxxxxxx'

    #发送邮箱,接收邮箱
    sender = 'xxxxxx@qq.com'
    receiver = 'xxxxxxxxx@163.com'

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("auto test result", 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
       
    smtp = smtplib.SMTP_SSL(smtpsever, 465)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("Success!")
    
#查找最新结果
def new_report(report_dir):
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + fn))
    file = os.path.join(report_dir, lists[-1])
    return file

if __name__ == '__main__':
    test_report = 'F:\\coding\\selenium\\result\\'
    new_report = new_report(test_report)
    send_email(new_report)




