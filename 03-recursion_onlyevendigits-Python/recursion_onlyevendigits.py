# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(lst):
	if (len(lst) == 0):
		return []
	newlst = []
	for i in lst:
		newlst.append(rec(str(i),'',0))
	return newlst
def rec(numm, res, i):
	if (i == len(numm)):
		if res == '':
			return 0
		return int(res)
	else:
		if ((int(numm[i]) % 2) == 0):
			return rec(numm, res + numm[i], i + 1)
		else:
			return rec(numm, res, i + 1)

if __name__ == "__main__":
	print(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))
