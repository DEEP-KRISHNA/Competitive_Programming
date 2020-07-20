# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
	# Your code goes here
	newlst = []
	lst = lookandsay(L)
	for i in lst:
		if (i[0] >= k):
			newlst.extend([i[1]] * (i[0] - k))
		else:
			newlst.extend([i[1]] * i[0])
	return newlst


def lookandsay(a):
	if (len(a) == 0):
		return []
	count = 1
	lst = []
	for i in range(1, len(a)):
	# print(a[i], a[i-1])
		if (a[i] == a[i - 1]):
			count = count + 1
		else:
			lst.append((count, a[i-1]))
			count = 1
	lst.append((count, a[i]))
	return lst

if __name__ == "__main__":
	print(shortenlongruns([2, 3, 5, 5, 5, 3], 2))
