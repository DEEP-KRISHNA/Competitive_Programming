# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    # return 0
    n = n + 1
    i = 0
    num = 1
    while (i < n):
        nu = str(num)
        flag = True
        for j in range(1, len(nu)):
            if (int(nu[j]) < int(nu[j - 1])):
                flag = False
                break
        if (flag):
            i = i + 1
        num += 1
    return num - 1

if __name__ == "__main__":
    print(fun_nth_tidynumber(100))
