# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	s = s.lower()
	dic = {}
	for i in s:
		if ((ord(i) >= 97) and (ord(i) <= 122)):
			if (i in dic):
				dic[i] += 1
			else:
				dic[i] = 1
	print(dic)
	lst = list(dic.values())
	if (len(lst) == 0):
		return ""
	lst.sort()
	retlst = []
	for i in dic:
		if (dic[i] == lst[0]):
			retlst.append(i)
	retlst.sort()
	return (''.join(retlst))
	# Your code goes here


if __name__ == "__main__":
	leastfrequentletters("aDq efQ? FB'daf!!!".upper())
