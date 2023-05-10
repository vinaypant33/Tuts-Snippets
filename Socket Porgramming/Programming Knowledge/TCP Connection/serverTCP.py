""" In here we will be making the client Server program




"""


import socket


server_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1' , 12345))
server_socket.listen(5) # here 5 is the backlog parameter 5 means 5 connections keep waiting if the server is busy and if 6th connection tries to connet then the server refuses 

while True: 
    print("Server waiting for connection")
    client_socket , addr = server_socket.accept()
    print("client connected from" , addr)
    while True:
        data  =  client_socket.recv(1024).decode()
        if not data or data.decode('utf-8') == 'END':
            break
        print("Received from client %s" %data.decode('utf-8'))
        try:
            client_socket.send(bytes("Hey Client and I am here" , 'utf-8'))
        except:
            print("Exited by the user")
        client_socket.close()
        server_socket.close()