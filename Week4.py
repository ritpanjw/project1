"""
template==
Find the divisors of the number given by user
"""

j=[1]
def divisor(num):
	for i in range(2, num):
		if num%i!=0:
			continue
	
		else:
			j.append(i)
	print j

number=raw_input("Tell me the number whose divisors you want :::: ")
num=int(number)
divisor(num)
