import socket
import sys
import pickle
import threading
import selectors

HOST = sys.argv[1]
PORT = int(sys.argv[2])

sel=selectors.DefaultSelector()

class reader(threading.Thread):
	"""docstring for reader"""
	def __init__(self):
		super(reader, self).__init__()
	def run(self):
		while True:
			data=input()
			#

class writer(threading.Thread):
	"""docstring for writer"""
	def __init__(self,soc):
		super(writer, self).__init__()
		self.soc=soc
	def run(self):

		

soc = socket.socket()
try:
	soc.connect((HOST,PORT))
except:
	print("Cannot connect to ",HOST," at port ",PORT)
	exit()
r=reader();
w=writer(soc);
r.start();
w.start();