# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def fun_nth_uglynumber(n):
    return 0


def factors(n):
	lst = []
	for i in range(2, int(math.sqrt(n)) + 1):
	    flag = False
	    while (n % i == 0):
	        n = n / i
	        flag = True
	    if (flag == True):
	        lst.append(i)
	if (n >= 1):
	    lst.append(int(n))
	return lst

def prime(num):
    if (num <= 1):
        return False
	
    for i in range(2, int(math.sqrt(num)) + 1):
	    if (num % i == 0):
	        return False
    return True
