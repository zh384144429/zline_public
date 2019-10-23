#!/usr/bin/python3
# -*- coding=utf-8 -*-

import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
print(ifconfig_result)

ipv4_add = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}',ifconfig_result)[0]
netmask = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}',ifconfig_result)[1]
broadcast = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}',ifconfig_result)[2]
mac_addr = re.findall('[a-f0-9]{2}[:][a-f0-9]{2}[:][a-f0-9]{2}[:][a-f0-9]{2}[:][a-f0-9]{2}[:][a-f0-9]{2}',ifconfig_result)[0]

format_string = '{0:<10}:{1:<16}'

print(format_string.format('ipv4_add',ipv4_add))
print(format_string.format('network',netmask))
print(format_string.format('broadcast',broadcast))
print(format_string.format('mac_addr',mac_addr))

ip_route = os.popen('ip route').read()
ipv4_gw = re.findall('via\s+(\d*\.\d*\.\d*\.\d*)',ip_route)[0]
# ipv4_gw1='10.255.255.1'
# print(ip_route)
# print(ipv4_gw)

print('\n我们假设网关IP地址为最后一位254，因此网关IP地址为:' + ipv4_gw + '\n')
#
ping_result = os.popen('ping ' + ipv4_gw +'  -c 1').read()

# print(ping_result)

re_ping_result = re.findall('=',ping_result)
# print(re_ping_result)
if re_ping_result == ['=', '=', '=', '=']:
    print('网关可达')
else:
    print('网关不可达')

