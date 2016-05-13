#!/usr/bin/python
#-*- coding: utf-8 -*-
#author 2016-05-04  完成转换成字符串，改开完成切成四段
import sys
import struct
import socket

# 将3232236031 转换成192.168.1.255,就算成功
def int2ip(num):
	#print reduce(lambda x,y:)
	print socket.inet_ntoa(struct.pack('I',socket.htonl(num)))
if __name__ == "__main__":
	num = int(sys.argv[1])
	int2ip(num)