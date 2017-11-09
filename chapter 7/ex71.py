# read and print the contents of a text file line by line

fhand = open('mbox-short.txt')

for line in fhand:
	line = line.rstrip()
	print(line);
