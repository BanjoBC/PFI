#Exercise 2: This program counts the distribution of the hour of the day 
#for each of the messages. You can pull the hour from the “From” line by
#finding the time string and then splitting that string into parts using 
#the colon character. Once you have accumulated the counts for each hour, 
#print out the counts, one per line, sorted by hour as shown below.

#open a file
try:
	fhand = open(input('Enter a file: '))

except:
	print('Please enter a valid file name')

# Make an empty list and dictionary
dlist = list()
ddict = dict()


#parse the lines and create count dictionary
for lines in fhand:
	words = lines.split()
	if len(words) == 0 or len(words) < 3 or words[0] != 'From' : continue 
	time = words [5]
	tbits = time.split(':')
	hour = tbits [0]
	ddict [hour] = ddict.get(hour,0)+1

#create a list of tuples, key value pairs
for k,v in list(ddict.items()):
	dlist.append((k,v))

#sort list in descending order
dlist.sort()

print(dlist)