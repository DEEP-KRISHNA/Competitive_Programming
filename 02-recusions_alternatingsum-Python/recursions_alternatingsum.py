# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(lst):
	if (len(lst) == 0):
		return 0
	return rec(lst, 0, 0)
	
def rec(lst, i, summ):
	if (i % 2 == 0):
		summ = summ + lst[i]
	else:
		summ = summ - lst[i]
	i = i + 1
	if (i == len(lst)):
		return summ
	else:
		return rec(lst, i, summ)

if __name__ == "__main__":
	print(fun_recursions_alternatingsum([5, 3, 8, 4]))
