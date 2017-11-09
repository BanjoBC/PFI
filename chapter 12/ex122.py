#Exercise 2: Change your socket program so that it counts the number of charac- ters it
#has received and stops displaying any text after it has shown 3000 characters. The 
#program should retrieve the entire document and count the total number ofcharacters and
#display the count of the number of characters at the end of the document.

import socket

try:
	wpage = input('enter url: ')
	wpieces = wpage.split('/')
	waddress = wpieces [2]
	print('debug',waddress)
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect((waddress, 80))
except:
	print('error improperly formated or non-existant url')
front = 'GET '
ending = ' HTTP/1.0\r\n\r\n'
gline = front+wpage+ending
cmd = gline.encode()
mysock.send(cmd)

numchar = 0
while True:
    data = mysock.recv(525)
    if (len(data) < 1):
        break
    print(data.decode())
    print(len(data.decode()))
mysock.close()

print(numchar)