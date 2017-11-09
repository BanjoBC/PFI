# exercise 6.2 make a function called counter that will count the number
# of letters in a string. the funtion should accept the letter and
# srting as arguments.

word = input('Please enter a word ')
letter = input('Please enter a letter ')
def count(w,l):
	numlet = 0
	for char in w:
		if char == l:
			numlet = numlet + 1
	return numlet
totlet = count(word,letter)
if totlet == 1:
	print('The letter '+letter+' occurs once in the word '+word+'.')
else:
	print('There are',totlet,'occurances of the letter '+letter+' in the word '+word+'.');
