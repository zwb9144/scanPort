#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

def ip2int(ip):
	#ip = sys.argv[1]
	return  reduce(lambda x,y:(x<<8)+y,map(int,ip.split('.')))