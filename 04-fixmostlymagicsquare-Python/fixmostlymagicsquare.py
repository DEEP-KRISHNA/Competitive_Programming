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
	for i in range(len(a[0])):
		summ1 = 0
		summ2 = 0
		for j in range(len(a[0])):
			summ1 = summ1 + a[i][j]
			summ2 = summ2 + a[j][i]
		dic[(i,0)] = summ1
		dic[(0,i)] = summ2
	lst.sort()
