#Write a function called chop that takes a list and modifies it, removing the first
#and last elements, and returns None.
#Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

letters = ['a','b','c','d','e','f','g','l']

def chop (a):
	del a[0]
	del a[len(a)-1]

chop(letters)

print(letters);

def middle(b):
	c = b[1:len(b)-1]
	return c

nlist = middle(letters)

print(nlist,letters);