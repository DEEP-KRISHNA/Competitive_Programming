# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

import math

def isperfectsquare(n):
	# your code goes here
	try:
		n = int(n)
		sq = str(math.sqrt(n))
		ind = sq.index(".")
		if (sq[ind:] == ".0"):
			return True
		else:
			return False
	except:
		return False

if __name__ == "__main__":
	print(isperfectsquare(100))
