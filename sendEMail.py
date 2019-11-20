from email.mime.text import MIMEText

from pip._vendor.distlib.compat import raw_input

msg = MIMEText('hello, send by python...', 'plain', 'utf-8')

from_addr = 'imei857@163.com'
password = 'LMwjc7922!'

smtp_server = 'smtp.163.com'
to_addr = 'wangjc_strive@163.com'

import smtplib

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
