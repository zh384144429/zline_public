#!/usr/bin/python3
# -*- coding=utf-8 -*-

import os
import paramiko
import re
from day9_1 import qytang_ssh

def ssh_get_route(ip,username,password):
    ssh_get_route_result = qytang_ssh(ip,username,password,cmd='nmcli d show ens33')
    find_gateway = re.findall('IP4.GATEWAY:\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ssh_get_route_result)
    # print(find_gateway) #先把需要的网关找出来，我觉得可以用split加上for循环来匹配但是逻辑上不太好理解，我觉得这个笨办法好用
    find_gateway_str = find_gateway[0]#由于出来的个列表，而且列表的内容比较多，我还要再筛选一次，但是我觉得还是比for循环好用
    # print(find_gateway_str)#我把想要的东西转成字符串，然后把字符串中想要的东西匹配出来
    need_gateway = re.match('IP4.GATEWAY:\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',find_gateway_str).groups()
    #转成元组后我就可以提取出来IP地址了
    print('网关为：\n'+ need_gateway[0])

if __name__ == '__main__':
    ssh_get_route('10.255.255.128','root','a.1')

