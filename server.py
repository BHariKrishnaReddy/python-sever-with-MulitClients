# server END
import socket
import threading

port = 1457
HEADER = 64
#server = "172.28.0.2" avoid hardcode
FORMAT ='utf-8'
DISCONNECT = "I'm Disconnecting"
SERVER = socket.gethostbyname(socket.gethostname())#without hardcode we can get directly from this line

print(f'IPV4 address of the system {SERVER} & hostname {socket.gethostname()}')
ADDR =('',port)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF_INET tells us what type of connection we are looking for..
#SOCK_STREAM is like to stream the data


server.bind(ADDR)
#binding sever and port to the socket

def handle_client(connection,addr):
  #Handles the all of th communtication in btwn clients
  print(f"New connection {addr} connected")

  connected = True
  while connected:
    msg_length = connection.recv(HEADER).decode(FORMAT)
    if msg_lenght:
      msg_length = int(msg_length)
      msg = connection.recv(msg_length).decode(FORMAT)
      if msg == DISCONNECT:
        connected = False
      print(f'[ {addr} ] {msg}')
      #send msg to clien
      connection.send("Text to send to client".encode(FORMAT))
  connection.close()
  



def start():
  #starts the socket server for us
  server.listen()
  print(f"Serever is listening on {SERVER}")
  while True:
    connection , addr = server.accept()
    #server.accept will wait for the connections and when ever connection occurs then we will store the address of the connectoin and an object
    thread = threading.Thread(target=handle_client() , args=(connection , addr ))
    thread.start()
    print(f"Active connections {threading.activeCount() - 1}")


print("Strating sever...")
start()
