# Exercise 3.3 prompt a score and return a grade. Example

try:
	score = input('Enter score:');
	float(score)
	if score >= 1:
		print('Bad score')
	else:
		if score >= 0.9:
			print('A')
		else:
			if score >= 0.8:
				print('B')
			else:
				if score >= 0.7:
					print('C')
				else:
					if score >= 0.6:
						print('D')
					else:
						if score >=0.0:
							print('F')
						else:
							print('Bad score');
except:
	print('Enter, numeric input');