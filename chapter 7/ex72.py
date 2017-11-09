# Prompt for a file name and search contents for a string.

inp = input('Enter a file name ')
try:
	fhand = open(inp)
	for line in fhand:
		line = line.rstrip()
		if line.find('X-DSPAM-Confidence:') == -1:
			continue
		line = float(line[19:])
		print(line)
except:
	print('Error, please enter a valid file name');
