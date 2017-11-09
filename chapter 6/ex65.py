# Exercise 6.5 use finnd and slice to extract a portion of a string

string = 'X-DSPAM-Confidence:0.8475'
col = string.find(':')
ext = string[col+1:]
num = float(ext)
print(num);



