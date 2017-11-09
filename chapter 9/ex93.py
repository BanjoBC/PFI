#Exercise 3: Write a program to read through a mail log, build 
#a histogram using a dictionary to count how many messages have 
#come from each emailaddress, and print the dictionary.


#Exercise 4: Add code to the above program to figure out who has 
#the most messages in the file.After all the data has been read 
#and the dictionary has been created, look through the dictionary 
#using a maximum loop (see Section [maximumloop]) to find who has 
#the most messages and print how many messages the person has.

try:
	fhand = open(input('Enter a file name: '))
except:
	print('Not a valid file name')

cnames = dict()

m = 0

for line in fhand:
	words = line.split()
	if len(words) == 0 or len(words) < 3 or words[0] != 'From' : continue 
	name = words [1]
	cnames [name] = cnames.get(name,0)+1
	
	for x in cnames:
		if cnames [x] <= m: continue
		m = cnames [x]
		k = x 

print(k,cnames [k])

