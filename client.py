import socket

port = 1456
HEADER = 64
FORMAT ='utf-8'
DISCONNECT = "I'm Disconnecting"

SERVER ="172.28.0.2" #socket.gethostbyname(socket.gethostname())
ADDR =(SERVER,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)
  send_length +=b' '*(HEADER - len(send_lenght))
  client.send(send_length)
  client.send(message)
  print(client.recv(2048))
send("Hello")
