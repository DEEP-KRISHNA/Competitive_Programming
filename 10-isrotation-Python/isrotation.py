# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	xstr = str(x)
	ystr = str(y)
	if (len(xstr) != len(ystr)):
		return False
	ynew = ystr + ystr
	return xstr in ynew

if __name__ == "__main__":
	lst = [
            (3412, 1234, True), (12345, 54321, True),
            (1234, 1234, True), (12345, 4321, False),
            (3142, 1234, False), (10010, 10100, True),
            (431256789, 123456789, False), (101111, 11110, False),
        ]
	for i in lst:
		if (isrotation(i[0], i[1]) != i[2]):
			print(i)
