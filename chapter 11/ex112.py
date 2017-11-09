#Exercise 2: Write a program to look for lines of the form
#`New Revision: 39772`
#and extract the number from each of the lines using a regular 
#expression and the findall() method. Compute the average of 
#the numbers and print out the average.
#Enter file:mbox.txt
#38549.7949721
#Enter file:mbox-short.txt
#39756.9259259

#import re module
import re

#open a file
try:
	fhand = open(input('enter a file: '))
except:
	print('invalid file')
#make and empty list
revcount = list()
#iterate through the lines and retrive the data
for line in fhand:
	line = line.rstrip()
	x = re.findall('^New Revision: ([0-9]*)',line)
	if len(x) > 0: revcount.extend(x)

#tried this and it didn't work, also had print debug statement
#for i in revcount:
	#int(i)
#print('debug',revcount, len(revcount),sum(int(i) for i in revcount))

#print and compute average
print(sum(int(i) for i in revcount)/len(revcount))

