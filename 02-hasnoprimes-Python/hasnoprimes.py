# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	for i in l:
		for j in i:
			if (is_prime(j)):
				return False
	return True

def is_prime(num):
	for i in range(2, int(num / 2) + 1):
		if (num % i == 0):
			return False
	return True

