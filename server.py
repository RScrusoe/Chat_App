import socket
import sys
import select
import pickle

RECV_BUFFER = 1024

HOST = socket.gethostname()
PORT = int(sys.argv[1])

server = socket.socket()
server.bind((HOST,PORT))
server.listen(1)
client,address = server.accept()
inputs=[client,sys.stdin]
while True:
	print("\nYou: ",end ="")
	readable,writable,exeptional = select.select(inputs,[],[])
	for r in readable:
		if r is client:
			print("\nOther: ",end="")
			print(pickle.loads(r.recv(RECV_BUFFER)))
		if r is sys.stdin:
			msg = input()
			client.send(pickle.dumps(msg))