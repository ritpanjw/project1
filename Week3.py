"""
template==
print out a new list with number less then what user entered
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

x=[]
def num_less_ten(num):
	"""
	for i in a:
		print i
		if i < num:
			x.append(i)
		else:
			continue
	print x
	"""
	[x.append(i) for i in a if i < num]
	print x

number=raw_input("Enter a number you want the output lesser then::::: ")
num=int(number)
num_less_ten(num)



	
