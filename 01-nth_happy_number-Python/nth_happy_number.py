# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

import math

def fun_nth_happy_number(n):
	n = n + 1
	req = 0
	i = 1
	while (req < n):
		if (ishappynumber(i)):
			req += 1
		i += 1
	return i-1


def ishappynumber(n):
	# your code goes here
	if (n < 0):
		n = n * -1
	if (n < 10):
		if (n == 1 or n==7):
			return True
		else:
			return False
	su = 0
	n = str(n)
	for i in n:
		su = su + math.pow(int(i), 2)
	return ishappynumber(int(su))

if __name__ == "__main__":
	print(fun_nth_happy_number(7))