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

# 邮件模板
msg = MIMEMultipart()
msg['subject'] = '邮件主题'
msg['from'] = sender
msg['to'] = receiver

f = open("文件路径")
mail_body = f.read()
f.close()

# 加附件
att = MIMEText(mail_body, 'base64', 'utf-8')
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename= “test_report.html"'
msg.attach(att)

# 邮件流程
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()