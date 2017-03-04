"""
template==
Compute if a number is even or odd
"""

def even_odd(num):
	if num%4==0:
		print "%s is a multiple of 4" %(num)
	elif num%2==0:
		print "%s is even" %(num)
	else:
		print "%s is odd" %(num)


a=raw_input("Enter the number which you want the code to run: ")
num=int(a)
even_odd(num)



