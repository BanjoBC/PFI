# Prompt for a file name and search contents for a string.
# then Take a desired portion of the string.

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
	if inp == 'na na boo boo':
		print("NA NA BOO BOO TO YOU - You have been punk'd!")
	print('Error, please enter a valid file name');
