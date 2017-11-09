#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
#Your program should convert all the input to lower case and only count the letters a-z. Your program 
#should not count spaces, digits, punctua- tion, or anything other than the letters a-z. Find text 
#samples from several different languages and see how letter frequency varies between languages. 
#Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.

#import string library
import string
#open a file
try:
	fhand = open(input('Enter a file: '))
except:
	print('Please enter a valid file name')
# Make an empty dictionary and list
ldict = dict()
llist = list()
#read each line of the file and clean it, make a list of all the letters and add them to the dictonary
for line in fhand:
	line = line.translate(str.maketrans('','',string.punctuation))
	line = line.lower()
	words = line.split()
	#print('debug',words)
	for word in words:
		#use tuple to break word into individual leters
		letters = tuple(word)
		#print('debug',letters)
		for letter in letters:
			ldict[letter] = ldict.get(letter,0)+1
#sort and print dictionary
for k,v in list(ldict.items()):
	llist.append((v,k))
#sort and print list
llist.sort(reverse=True)
print(llist);