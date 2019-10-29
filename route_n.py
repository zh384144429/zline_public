#!/usr/bin/python3
# -*- coding=utf-8 -*-
import os
import re

route_result = os.popen('route -n').read()
ipv4_gw = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',route_result)[1]

print('网关为:{0}'.format(ipv4_gw))

# ip_add = re.findall('\d*\.\d*\.\d*\.\d',route_result)[1]
# # print(ip_add)
# flags = re.findall('UG',route_result)[0]
# # print(flags)
# need = [ip_add,flags]
# if need in route_result:
#     print('网关为：'+ ipv4_gw )


