#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import poplib
from email.parser import Parser

email = 'yangbifei@touchdata.io'
password = 'yangbfyg'
pop3_server = 'mail.touchdata.io'

server = poplib.POP3(pop3_server)  # 连接到POP3服务器:

server.set_debuglevel(1)  # 可以打开或关闭调试信息:

print(server.getwelcome().decode('utf-8'))  # 可选:打印POP3服务器的欢迎文字:

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()
