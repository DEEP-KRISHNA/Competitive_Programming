# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 


import math

def fun_get_kth_digit(digit, k):
	# return 0
	pow = math.pow(10,k)
	rem = digit % pow
	pow = math.pow(10, k - 1)
	dig = rem / pow
	return dig