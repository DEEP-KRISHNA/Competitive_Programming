# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2




def fun_nth_palindromic_prime(n):
	# return 1
	i = 2
	n_i = -1
	while (n_i != n):
		if (isPrime(i)):
			itemp = str(i)
			if(itemp == itemp[::-1]):
				n_i += 1
		i += 1
	return i - 1


def isPrime(p):
	for i in range(2, int(p/2) + 1):
		if (p % i == 0):
			return False
	return True
