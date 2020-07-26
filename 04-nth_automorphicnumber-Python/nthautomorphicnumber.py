# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

import math

global lst
lst = [0,1,5,6]
global maxx
maxx = 4

def nthautomorphicnumbers(n):
	global lst
	global maxx
	n = n - 1
	if (n < maxx):
		print(lst)
		return lst[n]
	else:
		return "het=y"

def mul(nu):
	# nu = num
	if (nu == 0):
		return 0
	if (nu % 10 == 0):
		return nu+5
	lenn = len(str(nu))
	lst1 = []
	lst2 = []
	for i in range(lenn):
		den = 10 ** (lenn - i - 1)
		lst1.append(int(nu / den))
		lst2.append(nu)
		nu = nu % den
	summ = 0
	for i in range(lenn):
		summ = summ + ((lst1[lenn - 1 - i] * lst2[i]) * (10 ** i))
	# print(summ)
	return int(str(summ)[::-1][:lenn][::-1])

if __name__ == "__main__":
	lst = [
            (1, 0),
            (2, 1),
            (3, 5),
            (4, 6),
            (5, 25),
            (6, 76),
            (7, 376),
            (8, 625),
            (9, 9376),
            (10, 90625),
            (11, 109376),
            (12, 890625),
            (13, 2890625),
            (14, 7109376),
            (15, 12890625),
            (16, 87109376),
            (17, 212890625),
            (18, 787109376),
            (19, 1787109376),
            (20, 8212890625),
            (21, 18212890625),
            (22, 81787109376),
            (23, 918212890625),
            (24, 9918212890625),
            (25, 40081787109376),
            (26, 59918212890625),
            (27, 259918212890625),
            (28, 740081787109376),
        ]
	for i in lst:
		print(nthautomorphicnumbers(i[0]))
	# 	if (nthautomorphicnumbers(i[0]) != i[1]):
	# 		print(i)
	# print("done")
	# print(mul(9))

