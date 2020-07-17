# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	ret = ''
	for i in text:
		if (i not in ret):
			ret = ret + i
	return ret
	# pass

if __name__ == "__main__":
	print(removeduplicate("a a "))
