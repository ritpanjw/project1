"""
template==Ask the user for a raw-input and print if number is palindrome or not
"""

def palindrome(num):
	j=list(num.upper())
	print j
	if j[::1]==j[::-1]:
		print "String is a palindrome"
	else:
		print "Not a string"

inp=raw_input("Enter a string----:")
num=inp
print num
palindrome(num)

