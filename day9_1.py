#!/usr/bin/python3
# -*- coding=utf-8 -*-
import paramiko


def qytang_ssh(ip,username,password,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x
if __name__ == '__main__':
    print(qytang_ssh('10.255.255.128', 'root', 'a.1'))
    print(qytang_ssh('10.255.255.128','root','a.1',cmd='pwd'))
    # print(qytang_ssh('10.255.8.130', 'root', '11111111',cmd='nmcli'))

# ssh = paramiko.SSHClient()
# ssh.load_system_host_keys()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('10.255.8.130',port=22,username='root',password='11111111',timeout=5,compress=True)
#

