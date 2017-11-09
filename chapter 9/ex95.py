#Exercise 5: This program records the domain name (instead of the address)
#where the message was sent from instead of who the mail came from 
#(i.e., the whole email address). At the end of the program, print out 
#the contents of your dictionary.

try:
	fhand = open(input('Enter a file name: '))
except:
	print('Not a valid file name')

cdomain = dict()
email = list()

m = 0

for line in fhand:
	words = line.split()
	if len(words) == 0 or len(words) < 3 or words[0] != 'From' : continue 
	email = words [1]
	esplit = email.split('@')
	domain = esplit[1]
	cdomain [domain] = cdomain.get(domain,0)+1
	
for k in cdomain:
	print( k, cdomain[k])

