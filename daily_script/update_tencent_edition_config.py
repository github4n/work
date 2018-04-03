#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/3/26 16:45
# Author : lixingyun
import paramiko

LINUX_HOST = '10.10.23.14'

def connect():
    'this is use the paramiko connect the host,return conn'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        #        ssh.connect(host,username='root',allow_agent=True,look_for_keys=True)
        ssh.connect(LINUX_HOST, username='lxy', password='lxy', allow_agent=True)
        return ssh
    except:
        return None

def get_linux_time():
    ssh = connect()
    stdin, stdout, stderr = ssh.exec_command('vi ~/huomaotv/application/config/edition_config.php')
    return (stdout.read().decode())

t = get_linux_time()
print(t)