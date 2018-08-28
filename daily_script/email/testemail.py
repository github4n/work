#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/8/28 15:15
# Author : lixingyun
# Description :

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
from_addr = 'lixy66@hotmail.com'
password = '******'
# 输入收件人地址:
to_addr = '2638008778@qq.com'


msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(f'{from_addr}')
msg['To'] = _format_addr(f'{to_addr}')
msg['Subject'] = Header('LUCKY_PYTHON测试邮件', 'utf-8').encode()

server = smtplib.SMTP('smtp-mail.outlook.com', 25) # SMTP服务器，端口
server.set_debuglevel(1)

server.ehlo()  # 发送SMTP 'ehlo' 命令
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()