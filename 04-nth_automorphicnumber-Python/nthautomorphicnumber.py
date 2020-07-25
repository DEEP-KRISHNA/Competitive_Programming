# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

import math

global dic
dic = {}
global maxkey
maxkey = 0

def nthautomorphicnumbers(n):
	global maxkey
	global dic
	n = n + 1
	if (n <= maxkey):
		return dic[n]
	else:
		if (maxkey == 0):
			i = 0
			num = 1
		else:
			i = maxkey
			num = dic[maxkey] + 1
		# while (i < n):
		# 	nu = num
		# 	for i in range(len(str(nu))):


def mul(num):
	nu = num
	lenn = len(str(nu))
	summ = 0
	lst1 = []
	lst2 = []
	for i in range(lenn):
		den = 10 ** (lenn - i - 1)
		lst1.append(int(nu / den))
		lst2.append(nu)
		# summ = summ + (nu * int(nu / den))
		nu = nu % den
	summ = 0
	for i in range(lenn):
		oth = lenn - 1 - i
		print((lst1[oth] * lst2[i]))
		print((lst1[oth]*lst2[i]) * (10 ** i))
		summ = summ + ((lst1[oth]*lst2[i]) * (10 ** i))
	print(summ)

if __name__ == "__main__":
	mul(9376)

