file = '/usr/share/wordlists/rockyou.txt'
words = []
text = ""
with open(file,'r',encoding = "ISO-8859-1") as f:
	text = f.read()

text = text.split()

for x in text:
	if len(x) == 6:
		words.append(x)

for y in words:
	print(y)
