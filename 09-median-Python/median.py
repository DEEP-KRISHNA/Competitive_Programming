# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	if (len(a) == 0):
		return None
	elif (len(a) % 2 == 0):
		pos = int(len(a) / 2)
		return (a[pos] + a[pos-1])/2
	else:
		return a[int(len(a) / 2)]

if __name__ == "__main__":
	print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
