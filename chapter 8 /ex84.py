#Exercise 4: Download a copy of the file from www.py4e.com/code3/romeo.txt Write a program to open the 
#file romeo.txt and read it line by line. For each line,
#split the line into a list of words using the split function.
#For each word, check to see if the word is already in a list. If the word is not in
#the list, add it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.

try:
	fhand = open(input('Enter a file '))
	poetry = list()
	w1 = list()
	for line in fhand:
		w2 = line.split()
		w1.extend(w2)
	for i in range(len(w1)):
		if w1 [i] in poetry: continue
		poetry.append(w1[i])
	poetry.sort()
	print(poetry)
except:
	print('Please enter a valid file')