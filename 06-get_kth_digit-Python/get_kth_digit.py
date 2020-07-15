# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 


import math

def fun_get_kth_digit(digit, k):
	# return 0
	if (digit < 0):
		digit = digit * -1
	digit = str(digit)
	if (k >= len(digit)):
		return 0
	else:
		return int(digit[len(digit) - k - 1])

if __name__ == "__main__":
	for i in [(789, 0, 9), (789, 1, 8), (789, 2, 7), (789, 3, 0), (-789, 0, 9), (-780, 4, 0)]:
		if (fun_get_kth_digit(i[0], i[1]) != i[2]):
			print(fun_get_kth_digit(i[0], i[1]))
			print(i)
