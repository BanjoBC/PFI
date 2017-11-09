#Exercise 5: Write a program to read through the mail box data and when you find line 
#that starts with “From”, you will split the line into words using the split function. 
#We are interested in who sent the message, which is the second word on the From line.
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#You will parse the From line and print out the second word for each From line, 
#then you will also count the number of From (not From:) lines and print out a count at the end.

ncount = 0

try:

	fhand = open(input('enter a file '))
	for lines in fhand:
		text = lines.split()
		#print('debug',text)
		if len(text) == 0 or len(text) < 2 or text [0] != 'From': continue
		print(text [1])
		ncount = ncount + 1	

except:
	'Enter a valid file name '

print('There were ',ncount,'lines in the file that begin with the word from.');

