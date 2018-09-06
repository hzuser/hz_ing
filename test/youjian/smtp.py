# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# dir(smtplib)
# print (dir(smtplib))

# 参数配置
smtpserver = "smtp.qq.com"
port = 465
sender = "1994690887@qq.com"
psw = "nkzgciuwbzwgchag"
receiver = "869067630@qq.com"

body = "<pre><h1>测试报告，请查收~</h1></pre>"   #定义邮件正文为html格式

# 邮件模板
msg = MIMEText(body, 'html', 'utf-8')
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = "测试报告"

# 邮件流程
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()