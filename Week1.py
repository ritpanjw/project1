"""
template==
Files are saved in http://www.practicepython.org/exercises/
What will be my age at 100th year
"""
import time

x=raw_input("Enter your name ")
print x
y=raw_input("Enter your age ")
print y
y=int(y)
a=time.ctime()
a=a[20:]
a=int(a)
z=100-y
b=a+z
print "Hey %s you will turn 100 years in %s" %(x, b)

