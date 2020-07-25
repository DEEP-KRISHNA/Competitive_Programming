# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

import math

def nthcircularprime(n):
	n = n + 1
	i = 0
	num = 1
	# while (i < n):
	# 	nu = str(num)
	# 	for i in range(len(nu)):
	# 		left = nu[i:]
	# 		right = nu[:i]
	nu = "123456789"
	for i in range(len(nu)):
		left = nu[i:]
		right = nu[:i]
		print(left+right)
	# Your code goes here
	pass

def prime(num):
	if (num <= 1):
		return False
	for i in range(2, int(math.sqrt(num)) + 1):
		if (num % 1 == 0):
			return False
	return True
