# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	dic = {}
	for i in s:
		if i in dic.keys():
			dic[i] = dic[i] + 1
		else:
			dic[i] = 1
	lst = list(dic.values())
	lst.sort()
	lst = lst[::-1]
	print(lst[n])
	return 'a'

if __name__ == "__main__":
	fun_kth_occurrences("helllo woorld", 2)


