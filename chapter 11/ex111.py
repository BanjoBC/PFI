#Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
#Ask the user to enter a regular expression and count the number of lines that matched the
#regular expression:

#import regular expression module
import re

#open a file
fhand = open('mbox.txt')

# input regular expression
rexp = input('Enter a regular expression: ')

#create count variable
c = 0
#iterate through the file and find the data, if line matches regular expression count it
for line in fhand:
	line = line.rstrip()
	if re.search(rexp,line):
		c = c+1

#print count variable
print('mbox.txt had',c,'lines that matched',rexp)

#close file handle
fhand.close()
