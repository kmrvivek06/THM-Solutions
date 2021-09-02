# !/usr/bin/python3

import requests
import json

path = "http://10.10.169.100:3000/"

flag = ""

current_value=""

while True:
	r = requests.get(path+current_value)
	d = json.loads(r.text)
	if d['value'] != 'end':
		flag = flag + d['value']
		current_value = d['next']
	else:
		flag = flag + current_value
		break

print(flag)
