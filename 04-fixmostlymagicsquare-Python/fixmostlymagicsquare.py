# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	# pass
	# Your code goes here
	dic = {}
	for i in range(len(L[0])):
		summ1 = 0
		summ2 = 0
		for j in range(len(L[0])):
			summ1 = summ1 + L[i][j]
			summ2 = summ2 + L[j][i]
		dic[(i,"L")] = summ1
		dic[(i, "H")] = summ2
	val = list(dic.values())
	val.sort()
	commonval = val[int(len(val) / 2)]
	x = -1
	y = -1
	excessval = -1
	for i in dic:
		if (dic[i] != commonval):
			if (i[1] == 'L'):
				x = i[0]
			else:
				y = i[0]
			excessval = dic[i] - commonval
	L[x][y] = L[x][y] - excessval
	return L
		
	

if __name__ == "__main__":
	print(fixmostlymagicsquare(
		[[16, 3, 2, 13], [5, 10, 11, 18], [9, 6, 7, 12], [4, 15, 14, 1]]))
