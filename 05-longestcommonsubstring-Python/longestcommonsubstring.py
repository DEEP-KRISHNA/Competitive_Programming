# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    if ((len(s1) == 0) or (len(s2) == 0)):
        return ""
    if (len(s2) > len(s1)):
        temp = s1
        s1 = s2
        s2 = temp
    lst = []
    for i in range(1,len(s1)):
        j = 0
        flag = False
        while (j < len(s1)):
            temp = s1[j: j + i]
            if (len(temp) == i):
                if(temp in s2):
                    if (not flag):
                        lst = []
                        flag = True
                    lst.append(temp)
            j = j + 1
    lst.sort()
    print(lst)
    pass

if __name__ == "__main__":
    longestcommonsubstring("abcABC", "zzabZZAB")
