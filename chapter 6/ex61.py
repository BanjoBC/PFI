# exercise 6.1 write a while loop that works backwards printing each
# letter of a string on a seprate line.

fruit = 'Banana'
index = len(fruit) - 1
while index >= 0: 
	print(fruit[index])
	index = index - 1
print('done');

for char in fruit:
	print(char)
