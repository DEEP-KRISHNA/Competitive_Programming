# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	ret = ''
	i = 0
	while(i < len(s1)):
		if (s1[i: i + len(s2)] == s2):
			ret = ret + s3
			i = i + len(s2)
		else:
			ret = ret + s1[i]
			i = i + 1
		# print(ret)
	return ret
	

if __name__ == "__main__":
	fun_replace("helloworld123", "123", "345")

