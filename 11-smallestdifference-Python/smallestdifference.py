# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	a.sort()
	minn = 100000000
	for i in range(1, len(a)):
		# print(a[i], a[i-1], a[i] - a[i - 1])
		if (a[i] - a[i - 1] < minn):
			minn = a[i] - a[i - 1]
			# print(minn)
	return minn

if __name__ == "__main__":
	print(smallestdifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
