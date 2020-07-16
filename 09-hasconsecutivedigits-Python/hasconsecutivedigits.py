# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	if (n < 0):
		n = n * -1
	n = str(n)
	for i in range(1,len(n)):
		if (n[i] == n[i - 1]):
			return True
	return False		
	# pass