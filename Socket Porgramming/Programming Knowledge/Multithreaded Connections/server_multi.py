import socket
from _thread import *  ## Used to make multiple threads

server_socket  = socket.socket()

## Declaring the host and port for communications 

host  = "127.0.0.1"
port  = 1233
## Thread count used to track the number fo threads running  

thread_count  = 0 

try :
    server_socket.bind((host , port))
except socket.error as err:
    print(str(err))

print("Waiting for connection")
server_socket.listen(5)


def client_thread(connection):
    connection.send(str("Welcome to the server"))
    while True: 
        data  = connection.recv(2048)
        reply  ="Hello I am server" + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
