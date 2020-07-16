# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	dic = {}
	n = str(n)
	for i in n:
		if (i in dic.keys()):
			dic[i] = dic[i] + 1
		else:
			dic[i] = 1
	print(dic)

if __name__ == "__main__":
	mostfrequentdigit(5231123123123)
