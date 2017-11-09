#payroll program uses raw input for hours to coimpute pay at a given rate

hoursinp = input('Enter Hours');
rateinp = input('Enter Pay Rate');
hours = float(hoursinp)
payrate = float(rateinp)
payout = payrate*hours
overtime =  (40*payrate)+((hours-40)*payrate*1.5)
if hours > 40:
	print(overtime)
else:
	print(payout);

