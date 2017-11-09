#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines
#and pull out the addresses from the line. Count the number of messages from each 
#person using a dictionary. After all the data has been read, print the person with
#the most commits by creating a list of (count, email) tuples from the dictionary. 
#Then sort the list in reverse order and print out the person who has the most commits.

#open a file
try:
	fhand = open(input('Enter a file: '))

except:
	print('Please enter a valid file name')

#make empty list and dictonary
topdomain = list()
cdomain = dict()

#parse the lines and create count dictionary
for lines in fhand:
	words = lines.split()
	if len(words) == 0 or len(words) < 3 or words[0] != 'From' : continue 
	email = words [1]
	cdomain [email] = cdomain.get(email,0)+1

#create a list of tuples, key value pairs
for k,v in list(cdomain.items()):
	topdomain.append((k,v))
	#print('debug',topdomain)

#sort list in descending order
topdomain.sort(reverse=True)

print(topdomain [:1])