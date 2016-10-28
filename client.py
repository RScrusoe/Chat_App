import socket
import sys
import select
import pickle

HOST = "127.0.1.1"
PORT = int(sys.argv[1])
RECV_BUFFER = 30

server = socket.socket()
server.connect((HOST,PORT))

inputs=[server,sys.stdin]

while True:
	print("\nYou: ",end="")
	readable,writable,exceptional = select.select(inputs,[],[])
	for r in readable:
		if r is server:
			print("\nOther: ",end="")
			print(pickle.loads(r.recv(RECV_BUFFER)))
		if r is sys.stdin:
			msg = input()
			server.send(pickle.dumps(msg))