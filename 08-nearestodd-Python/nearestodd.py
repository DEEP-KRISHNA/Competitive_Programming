# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	floatt = n % 1
	intt = int(n - floatt)
	print(intt,floatt)
	if (intt % 2 == 1):
		return intt
	else:
		if (round(floatt, 2) == 0.00):
			return intt - 1
		return intt + 1

if __name__ == "__main__":
	print(fun_nearestodd(13.77))


