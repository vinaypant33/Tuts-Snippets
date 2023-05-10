# from socket import *  
# import socket
# import sys

# ## We can also make the bluetooth socket we have to specify the family as AF bluetooth
# s = socket.socket(family=AF_INET , type=SOCK_STREAM ,proto=0) # For UDP use the sock_d


## Socket using the error handling 

import socket
import sys

try: 
    sock  =socket.socket(family=socket.AF_INET , type=socket.SOCK_STREAM)
except socket.error as err:
    print("Failed" + err)
    sys.exit()

print("Socket Created")

target_host  = input("Enter the target host name")
target_port = input("Enter thr post name")

try:
    sock.connect((target_host , int(target_port)))
    print("Connected with the target and socket")
    sock.shutdown(2)
except socket.error as errr:
    print(errr)