# Here we will rewrite the previous function to be destructive. This version must not just call the nondestructive 
# version from above and then clear and replace the values in the original list. Instead, you must traverse the list 
# once and make the changes to the list as you go. With that in mind, write the destructive function shortenLongRuns(
# L, k) that takes a list L and a positive integer k, and destructively modifies L by removing any values in L that 
# would otherwise produce a run of k consecutive equal values in L. 
# For example:
# L = [2, 3, 5, 5, 5, 3] 
# shortenLongRuns(L, 2)
# assert(L == [2, 3, 5, 3])
# And: 
# L = [2, 3, 5, 5, 5, 3]
# shortenLongRuns(L, 3)
# assert(L == [2, 3, 5, 5, 3])


def destructiveshortenlongruns(L, k):
	# Your code goes here
	newlst = []
	lst = lookandsay(L)
	for i in lst:
		if (i[0] >= k):
			newlst.extend([i[1]] * (k-1))
		else:
			newlst.extend([i[1]] * i[0])
	return newlst


def lookandsay(a):
	if (len(a) == 0):
		return []
	count = 1
	lst = []
	for i in range(1, len(a)):
		if (a[i] == a[i - 1]):
			count = count + 1
		else:
			lst.append((count, a[i-1]))
			count = 1
	lst.append((count, a[i]))
	return lst
