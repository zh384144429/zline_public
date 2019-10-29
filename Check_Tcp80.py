#!/usr/bin/python3
# -*- coding=utf-8 -*-


import os
import re
import time

while True:
        check_result = os.popen('netstat -tunlp').read()
        # print(check_result) 验证得到的内容
        time.sleep(2)
        tcp80 = re.findall('tcp\s+\d+\s+\d+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:80',check_result)
        #TCP必须要匹配，80必须匹配
        ##找到tcp80
        # print(tcp80) 验证一下是否找到
        if tcp80: #如果tcp80里面有内容 就是真的
        #想用这个 if tcp80 == True: 如果tcp80是真的往下执行，但是不好用。
            print('HTTP （TCP/80）服务已经被打开')
            break #打印后退出
        else:#如果这里没有内容，或者匹配不到80就是假的
            print('等待一秒钟重新开始监控')



