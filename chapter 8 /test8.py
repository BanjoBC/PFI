#test file for chapter 8

#Exercise 6: Rewrite the program that prompts the user for a 
#list of numbers and prints out the maximum and minimum of the numbers at
#the end when the user enters “done”. Write the program to store the numbers 
#the user enters in a list and use the max() and min() functions to 
#compute the maximum and minimum numbers after the loop completes.

numlist = list()

while True:
	try:
		inp = input('Enter a number or done to exit. ')
		numinp = float(inp)
		#print('debug',numinp,numlist)
		numlist.append(numinp)
	except:
		if inp == 'done':
			break
		else:	
			print('Error, please enter numeric input.')
			continue
high = max(numlist)
low = min(numlist)
print('maximum: ',high,'\nminimum: ',low)

