import socket
import sys
import select
import pickle

HOST = "127.0.1.1"
PORT = int(sys.argv[1])
RECV_BUFFER = 1024

def createConnection(server):
	server.connect((HOST,PORT))
	name = input("Enter username: ")
	server.send(pickle.dumps({"name":name}))

server = socket.socket()
createConnection(server)

inputs=[server,sys.stdin]

while True:
	readable,writable,exceptional = select.select(inputs,[],[])
	for r in readable:
		if r is server:
			msg = pickle.loads(server.recv(RECV_BUFFER))
			try:
				msg,sender = msg.split('@')
			except:
				sender = "SERVER"
			msg=msg.strip()
			sender=sender.strip()
			print(sender,":",msg)
		if r is sys.stdin:
			msg = input()
			print("You: ",msg)
			server.send(pickle.dumps(msg))