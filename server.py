import socket
import sys
import pickle
import threading

HOST = socket.gethostname()
PORT = sys.argv[1]

class ServerClass(threading.Thread):
	"""Class for creating threads for working with clients"""
	MSG_SIZE = 70
	def __init__(self,port,tID,addr):
		super(ServerClass, self).__init__()
		self.tID=tID
		self.addr=addr
		self.port=port
		self.soc=socket.socket()
	def run(self):
		self.soc.bind((HOST,int(port)))
		self.soc.listen(1)
		try:
			conn,naddr=self.soc.accept()
			if self.addr!=naddr
				raise Exception("Address does not match")
		except Exception as inst:
			self.soc.close()
			print(inst)
			exit()
		data="0"
		while data != '':
			data = self.soc.recv(MSG_SIZE)
			if Data is not None:
				print(data)

		

nofOfConnections=0;
threadsList=[]
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
while True:
	print("Waiting for connections (Total Connections: ",nofOfConnections,") ):")
	conn,addr = s.accept()
	if conn is not None:
		print("[+1] Connected to ",addr)
		conn.send(str(PORT+1)+'\n')
		nofOfConnections+=1
		print("Total connections: ",nofOfConnections)
		tempThread = ServerClass(PORT+1,nofOfConnections-1,addr)
		PORT+=1
		tempThread.start()
		threadsList.append(tempThread)
