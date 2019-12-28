#!/usr/bin/python3

import socket
target_ip="192.168.43.63"
target_port=1233


# now we are creating UDP socket -- this is for all sender and receiver both
#                   ipv4      ,     UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


# this is for senders
msg=input("ENTER YOUR MESSAGE: ")
# we have to encode the string to byte like object in python3 only

new_msg=msg.encode('ascii')
# now we can send to target
s.sendto(new_msg,(target_ip,target_port))
print(s.recvfrom(100))
