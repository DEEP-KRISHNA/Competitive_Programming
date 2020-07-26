# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def getallpermutations(x):
	# Your code goes here
	for i in range(len(x)):
		print(x[i], x[:i] + x[i + 1:])


if __name__ == "__main__":
	getallpermutations("abcd")
