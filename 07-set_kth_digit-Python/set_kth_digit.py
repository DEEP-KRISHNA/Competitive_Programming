# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
		sigflag = False
		if (n < 0):
			sigflag = True
			n = n * -1
		n = str(n)
		if (k > len(n)):
			return - 1
		elif (k == len(n)):
			n = str(d) + n[len(n) - k:]
		else:
			n = n[: len(n) - k - 1] + str(d) + n[len(n) - k :]
		if (sigflag):
			return int(n) * -1
		else:
			return int(n)
			

