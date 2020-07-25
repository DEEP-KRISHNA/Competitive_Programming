# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

import math

def fun_nth_uglynumber(n):
	i = 0
	n = n + 1
	num = 0
	while (i < n):
		if (prime_factors(num)):
			i += 1
		num += 1
	return num-1

def prime_factors(n):
	n_org = n
	if (n == 0):
		return False
	if (n == 1):
		return True
	for i in range(2, int(math.sqrt(n)) + 1):
		flag = False
		while (n % i == 0):
			n = n / i
			flag = True
		if (flag):
			if (not prime(i)):
				return False
	if (n > 2):
		if (not prime(n)):
			return False
	return True

def prime(num):
    return num in [2,3,5]

if __name__ == "__main__":
	print(fun_nth_uglynumber(0))