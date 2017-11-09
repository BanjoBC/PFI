#Exercise 2: Write a program that categorizes each mail message by which 
#day of the week the commit was done. To do this look for lines that start 
#with “From”, then look for the third word and keep a running count of each
#of the days of the week. At the end of the program print out the contents
#of your dictionary (order does not matter).

try:
	fhand = open(input('Enter a file name: '))
except:
	print('Not a valid file name')

cdays = dict()
#check = list()

for line in fhand:
	words = line.split()
	if len(words) == 0 or len(words) < 3 or words[0] != 'From' : continue 
	day = words [2]
	#check.append(day)
	cdays [day] = cdays.get(day,0)+1

for x in cdays:
	print(x,cdays[x])

#print(check)