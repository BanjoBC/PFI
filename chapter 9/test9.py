#test file for chapter 9 

#Exercise 1: [wordlist2]
#Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
#It doesn’t matter what the values are. Then you can use the in operator as a fast way to 
#check whether a string is in the dictionary.

fhand = open("words.txt")
wlist = list()
wordlist2 = dict()
for lines in fhand:
	w = lines.split()
	wlist.extend(w)
	
#print(wlist)
for x in wlist:
	wordlist2 [x] = ''

#print(wordlist2)

for y in wlist:
	if y  in wordlist2: continue
	print(y)
