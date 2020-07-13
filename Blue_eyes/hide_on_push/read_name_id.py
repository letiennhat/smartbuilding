import threading
while 1:
	text = open('name_id.txt','r+')
	print(text.readline())
	text.close()