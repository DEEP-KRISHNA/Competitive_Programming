# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def nthlychrelnumbers(n):
	# your code goes here
	num = 123
	i = 0
	while (i < n):
		if (lycherel_check(num)):
			i += 1
		num += 1
	return num - 1

def lycherel_check(num):
	for i in range(25):
		pal = int(str(num)[::-1])
		if (num == pal):
			return False
		num = num + pal
	return True

if __name__ == "__main__":
	print(nthlychrelnumbers(45))
