#!/usr/bin/python3
# -*- coding=utf-8 -*-

from day8_3 import qytang_ping
from day9_1 import qytang_ssh
import re
import pprint
from kamene.all import *

def qytang_get_if(*ips,usename='root',password='a.1'):
    # device_if_dict = {}
    for ip_reult in ips:  #如果IP地址多个，就把其中一个IP地址赋值成这个IP地址，
        print(ip_reult)   #验证一下导入的是否正常
        get_ping_reult = qytang_ping(ip_reult) #并且把赋值的IP地址导入qytang函数中
        print(get_ping_reult)
        # if get_ping_reult[1]:
        #     get_interface = qytang_ssh(ip_reult,username=usename,password=password,cmd='nmcli d')
        #     print(get_interface)

    # for ssh_ping_result in qytang_ping(ips):
    #     print(ssh_ping_result)
    #     if ssh_ping_result:
    #         ssh_result = qytang_ssh(ips,username='root',password='11111111')
    #         print(ssh_result)


    # return device_if_dict

if __name__ == "__main__":
    # pprint.pprint(qytang_get_if('10.255.8.1','10.255.8.2',usename='root',password='111111111'),indent=4)
    qytang_get_if('10.255.8.130','10.255.8.3', usename='root', password='a.1')
    # qytang_get_if('10.255.8.2', usename='root', password='11111111')
