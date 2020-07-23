# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	if (n < 0):
		n = n * -1
	lst = []
	for i in str(n):
		lst.append(i)
	look = lookandsay(lst)
	final = []
	for i in look[0]:
		if (i[0] == look[1]):
			final.append(i[1])
	final.sort()
	return final[0]
	# Your code goes here
	pass


def lookandsay(a):
	maxx = 0
	count = 1
	lst = []
	if (len(a) == 0):
		return (lst,maxx)
	for i in range(1, len(a)):
		# print(a[i], a[i-1])
		if (a[i] == a[i - 1]):
			count = count + 1
		else:
			if (count > maxx):
				maxx = count
			lst.append((count, a[i-1]))
			count = 1
	lst.append((count, a[i]))
	return (lst,maxx)


if __name__ == "__main__":
	print(lookandsay([-1, 2, 7]))
