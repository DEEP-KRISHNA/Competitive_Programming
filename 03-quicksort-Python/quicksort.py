"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	array.sort()
	return array

if __name__ == "__main__":
	print(quicksort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
