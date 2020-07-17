# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	first = str1[0]
	if (first not in str2):
		return False
	count = 0
	for i in str2:
		if (i == first):
			new = str2[count:] + str2[:count]
			if (str1 == new):
				return True
		count += 1
	return False

if __name__ == "__main__":
	print(isrotated("XYZ", "ZXY"))
