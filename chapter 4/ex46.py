# Excercise 4.6 turn payroll program into a function that takes
# hours and rate as input

def computepay (h,r):
	if h > 40:
		p = ((h * r )+ ((h-40)* r * 0.5))
	else:
		p = h * r
	return p

try:
	hinp = input('Enter hours: ');
	rinp = input('Enter rate: ');
	float(hinp)
	float(rinp)
except:
	print('Error, please enter a number')
	quit()
pay = computepay(hinp,rinp)

print(pay);
