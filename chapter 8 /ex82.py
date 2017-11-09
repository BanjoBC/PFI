# find an issue with the code by modifying text file and correct it

fhand = open('mbox-short copy.txt') 
count = 0
for line in fhand:
	words = line.split()
	# print 'Debug:', words
	if len(words) == 0 : continue
	if len(words) < 3 : continue
	if words[0] != 'From' : continue 
	print(words[2])