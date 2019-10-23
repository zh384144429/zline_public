#!/usr/bin/python3
# -*- coding=utf-8 -*-
import os
import re

route_result = os.popen('route -n').read()
ipv4_gw = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',route_result)[1]

print('网关为:{0}'.format(ipv4_gw))