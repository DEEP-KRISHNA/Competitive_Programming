# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of 
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character 
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is 
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either 
# parameter is not a string, but returns True if both strings are empty (why?).

def samechars(s1, s2):
	s1 = str(s1)
	s2 = str(s2)
	# Your code goes here
	return (s1 in s2) or (s2 in s1)


if __name__ == "__main__":
	lst = [
            (("abcabcabc", "cab"), True),
            (("abcabcabc", "cbad"), False),
            (("abcabcabc", "cBa"), False),
            ((42, "The other parameter is not a string"), False),
            (("", ""), True),
        ]
	for i in lst:
		print(samechars(i[0][0],i[0][1]))
