"""
UDP is the connection less sever and client 



"""
import socket

sock  = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
sock.bind(('127.0.0.1' , 12345))


while True : 
    data, addr  = sock.recvfrom(4096) # In thi there are two things but as it has UDP we only have the data we have define the bytes 
    print(data)
    message  = bytes("Hello I am UDP Server").encode('utf-8')
    sock.sendto(message , addr)
    