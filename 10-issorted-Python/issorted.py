# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	b = a.copy()
	c = a.sort()
	print(c)
	return a == b

if __name__ == "__main__":
	print(issorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
