# Exercise 4.7 prompt a score and return a grade. using a defined
#called compute grade.

def computegrade(s):
	if s >= 1:
		grade ='Bad score'
	else:
		if s >= 0.9:
			grade = 'A'
		else:
			if s >= 0.8:
				grade = 'B'
			else:
				if s >= 0.7:
					grade = 'C'
				else:
					if s >= 0.6:
						grade = 'D'
					else:
						if s >=0.0:
							grade = 'F'
						else:
							grade = 'Bad score'
	return grade

try:
	score = input('Enter score:');
	float(score)
	
except:
	print('Enter, numeric input');
	quit()

finalgrade = computegrade(score)

print(finalgrade);