# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

import math

def largestperfectsquare(n):
	# your code goes here
	# pass
	dec = math.sqrt(n) % 1
	inte = math.sqrt(n) - (math.sqrt(n) % 1)
	if (dec == 0.0):
		return n
	# elif (dec > 0.5):
	# 	return int(math.pow(inte + 1,2))
	else:
		return int(math.pow(inte, 2))
		
if __name__ == "__main__":
	print(largestperfectsquare(5))
