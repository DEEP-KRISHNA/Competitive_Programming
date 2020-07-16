# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



import math
def fun_nth_happy_prime(n):
	n = n + 1
	req = 0
	i = 6
	while (req < n):
		if (isPrime(i) and ishappynumber(i)):
			req += 1
		i += 1
	return i-1


def isPrime(num):
	for i in range(2,int(num / 2)+1):
		if (num % i == 0):
			return False
	return True


def ishappynumber(n):
	# your code goes here
	if (n < 0):
		n = n * -1
	if (n < 10):
		if (n == 1 or n == 7):
			return True
		else:
			return False
	su = 0
	n = str(n)
	for i in n:
		su = su + math.pow(int(i), 2)
	return ishappynumber(int(su))
	
if __name__ == "__main__":
	print(fun_nth_happy_prime(4))
