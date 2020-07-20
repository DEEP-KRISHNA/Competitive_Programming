# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def fun_nth_additive_prime(n):
	# return 1
	i = 2
	n_i = -1
	while (n_i != n):
		if (isPrime(i)):
			itemp = str(i)
			summ = 0
			for j in itemp:
				summ = summ + int(j)
			if (isPrime(summ)):
				n_i += 1
		i += 1
	return i -1

def isPrime(p):
	for i in range(2, int(p/2) + 1):
		if (p % i == 0):
			return False
	return True