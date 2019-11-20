from email.mime.text import MIMEText
msg = MIMEText('hello，send by python...','plain','utf-8')

#发送邮箱地址
from_addr = 'imei857@163.com'

#邮箱授权码，非登陆密码
password = 'wjc8565857'

#收件箱地址
to_addr = 'wangjc_strive@163.com'

#smtp服务器
smtp_server = 'smtp.163.com'
#发送邮箱地址
msg['From'] = from_addr
#收件箱地址
msg['To'] = to_addr
#主题
msg['Subject'] = 'the frist mail'
import smtplib

server = smtplib.SMTP(smtp_server,25)

server.set_debuglevel(1)

print(from_addr)
print(password)
server.login(from_addr,password)

server.sendmail(from_addr,[to_addr],msg.as_string())

server.quit()
