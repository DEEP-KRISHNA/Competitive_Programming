# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

import math

global dic
dic = {}
global maxkey
maxkey = 0

def nthcircularprime(n):
	global maxkey
	global dic
	n = n + 1
	if (n <= maxkey):
		print(dic)
		return dic[n]
	else:
		if (maxkey == 0):
			i = 0
			num = 1
		else:
			i = maxkey-1
			num = dic[maxkey]-1
		while (i < n):
			nu = str(num)
			if('0' not in nu):
				flag = True
				for j in range(len(nu)):
					left = nu[j:]
					right = nu[:j]
					# print(num,left+right)
					if (not prime(int(left + right))):
						flag = False
				if (flag):
					i = i + 1
					dic[i] = num
					maxkey = i
				# print(i,num)
			num = num + 1
		return num - 1

def prime(num):
	if (num <= 1):
		return False
	for i in range(2, int(math.sqrt(num)) + 1):
		if (num % i == 0):
			return False
	return True

if __name__ == "__main__":
	print(nthcircularprime(46))
