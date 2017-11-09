#Exercise 5.1 Write a program that excepts numbers as input until done
#is entered then output sum, count and average

total = 0
count = 0
smallest = None
largest = None
while True:
	try:
		inp = input('Enter a number or done to exit. ')
		numinp = float(inp)
	except:
		if inp == 'done':
			break
		else:	
			print('Error, please enter numeric input.')
			continue
	total = total + numinp
	count = count + 1
	if largest is None or largest < numinp:
		largest = numinp
	if smallest is None or smallest > numinp:
		smallest = numinp
print('Total',total,'count',count,'min',smallest,'max',largest);

