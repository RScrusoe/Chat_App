import socket
import select
import sys
import threading
import time

class writer(threading.Thread):
	"""docstring"""
	def __init__(self):
		super(writer,self).__init__()
	def run(self):
		ptime=time.gmtime().tm_sec
		ctime=time.gmtime().tm_sec
		while (ptime+5)%60 != ctime:
		#	print(ptime,(ptime+5)%60,ctime)
			ctime=time.gmtime().tm_sec
		#cur_msg=sys.stdin.read()
		print("Hello")
		#sys.stdin.write("cur_msg")
for line in sys.stdin:
	print(line)	