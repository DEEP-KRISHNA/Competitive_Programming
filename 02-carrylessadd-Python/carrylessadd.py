# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	xstr = str(x)
	ystr = str(y)
	xflag = False
	minlen = len(xstr)
	if (len(xstr) > len(ystr)):
		xflag = True
		minlen = len(ystr)
	res = ''
	for i in range(minlen):
		res = res + str(int(xstr[i])+int(ystr[i]))[-1]
	if (xflag):
		maxx = len(xstr) - minlen
		return int(xstr[:maxx] + res)
	return int(res)