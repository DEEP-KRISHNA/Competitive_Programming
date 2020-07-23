# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

import math

def fun_nth_smithnumber(n):
    n = n + 1
    i = 0
    num = 3
    while (i < n):
        lst = prime_factor(num)
        sum1 = 0
        if(len(lst)!=1):
            for j in lst:
                sum1 = sum1 + j
            sum2 = 0
            for j in str(num):
                sum2 = sum2 + int(j)
            if (sum1 == sum2):
                i = i + 1
        num += 1
    return num-1

def prime_factor(n):
    lst = []
    while (n % 2 == 0):
        lst.append(2)
        n = n / 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while (n % i == 0):
            lst.append(int(i))
            n = n / i
            
    if (n > 2):
        lst.append(int(n))
    return lst

if __name__ == "__main__":
    print(fun_nth_smithnumber(1))
    print(prime_factor(22))
