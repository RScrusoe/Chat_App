import socket
import sys
import select
import pickle

RECV_BUFFER = 1024

HOST = socket.gethostname()
PORT = int(sys.argv[1])

def getclientname(client):
	msg = client.recv(RECV_BUFFER)
	clientdata = pickle.loads(msg)
	return clientdata["name"]

def getNameFromClient(client,clients):
	for item in clients:
		if item["client"] is client:
			return item["name"]
	return ""

def NameIsNotPresent(name,clients):
	for client in clients:
		if client["name"] == name:
			return False
	return True

server = socket.socket()
server.bind((HOST,PORT))
print("Server started at",HOST,"on port",PORT)
server.listen(5)
print("Listening for incoming connections...")
inputs=[server]
clients=[]
while True:
	readable,writable,exeptional = select.select(inputs,[],[])
	for r in readable:
		if r is server:
			client,address = server.accept()
			name = getclientname(client)
			if NameIsNotPresent(name,clients):
				clients.append({"name":name,"client":client,"address":address})
				print("Client added: name:",name,"address:",address)
				client.send(pickle.dumps("Connection successful"))
				inputs.append(client)
			else:
				print("Client already exists with same name")
				client.send(pickle.dumps("User with same name already exists.\nConnection Closed\n"))
				client.close()
		else:
			msg = pickle.loads(r.recv(RECV_BUFFER))
			name,msg=msg.split('@')
			name=name.strip()
			msg=msg.strip()
			if NameIsNotPresent(name,clients):
				r.send(pickle.dumps("User with username: "+name+" is offline"))
				continue
			else:
				for client in clients:
					if client["name"] == name:
						sender = getNameFromClient(r,clients)
						msg=msg+"@"+sender
						client["client"].send(pickle.dumps(msg))
						msg=msg.split('@')[0]
						print("Sent to",name,"message: \"",msg,"\" from",sender)
						break
