# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	# Your code goes here
	n = rec(0, n)
	if (n == 0):
		return None
	else:
		lst = []
		for i in range(n):
			lst.append(3**i)
		return lst

def rec(i, n):
	if ((3 ** i) > n):
		return i
	else:
		return rec(i + 1, n)

if __name__ == "__main__":
	recursion_powersof3ton(0)
	recursion_powersof3ton(-42)
	recursion_powersof3ton(0.99)
	recursion_powersof3ton(1)
	recursion_powersof3ton(8.99)
	recursion_powersof3ton(9)
	recursion_powersof3ton(100)




