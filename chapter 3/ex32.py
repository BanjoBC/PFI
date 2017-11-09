#payroll program uses raw input for hours to coimpute pay at a given rate

try:
	hoursinp = input('Enter Hours ');
	rateinp = input('Enter Pay Rate ');
	float(hoursinp)
	float (rateinp)
	payout = (rateinp*hoursinp)
	overtime =  (40*rateinp)+((hoursinp-40)*rateinp*1.5)
	if hoursinp > 40:
		print(overtime)
	else:
		print(payout)
except:
	print('Error, please enter numeric input.');
