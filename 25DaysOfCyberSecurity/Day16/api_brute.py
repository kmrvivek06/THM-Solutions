#! /bin/python3

import requests

for i in range(1,100,2):
	html = requests.get(f'http://10.10.181.251/api/{i}')
	print(html.text)
