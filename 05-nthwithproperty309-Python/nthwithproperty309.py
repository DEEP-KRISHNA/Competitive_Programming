# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	n = n + 1
	i = 0
	num = 308
	while (i < n):
		poww = num ** 5
		flag = [False for i in range(10)]
		for j in str(poww):
			flag[int(j)] = True
		if(False not in flag):
			i = i + 1
		num += 1
	return num - 1
		

if __name__ == "__main__":
	print(nthwithproperty309(0))