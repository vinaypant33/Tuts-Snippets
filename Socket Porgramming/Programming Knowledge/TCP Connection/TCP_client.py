import socket
client_socket  = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1' , 12345))     # The posrt nuber has to be the same in which the server is running


## Sending the data to the server adn receiving the same 
payload  = "Hey Server I am a message from client"



try:
    while True:
        client_socket.send(payload.encode('utf-8'))
        data  =  client_socket.recv(1024).decode()
        print(str(data))
        more  = input("Do you want to send more messages : ")
        if more == 'yes':
            payload = input("Enter Message Plese ")
        else:
            break
except KeyboardInterrupt:
    print("Exited by the user")
client_socket.close()


