# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

import math

global dic
dic = {}
global maxkey
maxkey = 0

def nthcircularprime(n):
	global maxkey
	global dic
	n = n + 1
	if (n <= maxkey):
		# print(dic)
		return dic[n]
	else:
		if (maxkey == 0):
			i = 0
			num = 1
		else:
			i = maxkey
			num = dic[maxkey]+1
		while (i < n):
			nu = str(num)
			if('0' not in nu):
				flag = True
				for j in range(len(nu)):
					left = nu[j:]
					right = nu[:j]
					# print(num,left+right)
					if (not prime(int(left + right))):
						flag = False
				if (flag):
					i = i + 1
					dic[i] = num
					maxkey = i
				# print(i,num)
			num = num + 1
		return num - 1

def prime(num):
	if (num <= 1):
		return False
	for i in range(2, int(math.sqrt(num)) + 1):
		if (num % i == 0):
			return False
	return True

if __name__ == "__main__":
	lst = [
            (0, 2), (1, 3), (2, 5), (3, 7),
            (5, 13), (6, 17), (7, 31), (8, 37),
            (9, 71), (10, 73), (11, 79), (12, 97),
            (13, 113), (14, 131), (15, 197), (16, 199),
            (17, 311), (18, 337), (19, 373), (20, 719),
            (21, 733), (22, 919), (23, 971), (24, 991),
            (25, 1193), (26, 1931), (27, 3119), (28, 3779),
            (29, 7793), (30, 7937), (31, 9311), (32, 9377),
            (33, 11939), (34, 19391), (35, 19937), (36, 37199),
            (37, 39119), (38, 71993), (39, 91193), (40, 93719),
            (41, 93911), (42, 99371), (43, 193939), (44, 199933),
            (45, 319993), (46, 331999), (47, 391939)
        ]
	for i in lst:
		if (nthcircularprime(i[0]) != i[1]):
			print(i)

	
