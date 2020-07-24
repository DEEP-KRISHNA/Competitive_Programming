# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math

def nthpowerfulnumber(n):
	if (n == 0):
		return 1
	# Your code goes here
	n = n + 1
	i = 1
	num = 1
	# while (i < n):
	# 	lst = factors(num)


def factors(n):
	lst = []
	for i in range(2, int(math.sqrt(n)) + 1):
		flag = False
		while (n % i == 0):
			n = n / i
			flag = True
		if (flag == True):
			lst.append(i)
	if (n > 2):
		lst.append(int(n))
	return lst

if __name__ == "__main__":
	print(factors(568))