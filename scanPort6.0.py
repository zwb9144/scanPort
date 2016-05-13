#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import struct
import threading
import socket
from time import sleep, ctime


#将一个整数转换成IP地址
def int2ip(num):
	#print reduce(lambda x,y:)
	return socket.inet_ntoa(struct.pack('I',socket.htonl(num)))
#将一个IP地址转换成整数
def ip2int(ip):
	#ip = sys.argv[1]
	return  reduce(lambda x,y:(x<<8)+y,map(int,ip.split('.')))

#该函数依次扫描每一个IP，当该端口开放时输出
def tcp_test(port,start_ip, end_ip):

	for target_ip in range(start_ip, end_ip+1):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(10)
		result = sock.connect_ex((int2ip(target_ip),port))
		if result == 0:
			print "Opened IP: port: ",int2ip(target_ip),": ",port
			#print int2ip(target_ip)
		sock.close()
#将一个数组分成n个均分的数组的函数,
#传入一个需要分割的次数n，将数据分成N份,最终生成N个列表，将给每个线程使用
def div_group(group,n):

	#group = [192.168.1.1 - 192.168.1.255]
	gs = []
	if len(group)%n == 0:
		for i in range(n):
			gs.append(group[i*(len(group)/n):(i+1)*(len(group)/n)])
	elif len(group)%n != 0:
		for i in range(n):
			if i != n-1:
				gs.append(group[i*(len(group)/n):(i+1)*(len(group)/n)]) 
			else:
				gs.append(group[i*(len(group)/n):])
	return gs

def main():
	# scanPort*.py <target_port> <start_ip-- end_ip> <线程数>
	print 'starting at:', ctime()
	#获取需要测试的端口
	target_port = int(sys.argv[1])
	#获取线程数
	n = int(sys.argv[3])
	#获取IP列表，生成一个数字的范围。 range()函数默认不带最后一个数字，所以加1
	group = range(ip2int(sys.argv[2].split('-')[0]),ip2int(sys.argv[2].split('-')[1])+1)
	# 根据线程数n使用切隔函数将数据切成相应的份数
	gs2=div_group(group,n)
	print gs2
	threads = []


	for j in range(n):
		#传递参数给函数，然后放到线程中
		t = threading.Thread(target=tcp_test,args=(target_port,gs2[j][0],gs2[j][-1]))
		threads.append(t)

	for j in range(n):
		threads[j].start()

	for j in range(n):
		threads[j].join()

	print "all DONE at:",ctime()

if __name__ == '__main__':
	main()