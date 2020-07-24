# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def fun_nth_lefttruncatableprime(n):
    n = n + 1
    i = 0
    numm = 1
    while (i < n):
        num = str(numm)
        count = 0
        for j in range(len(num)):
            temp = int(num[j:])
            if (prime(temp)):
                count += 1
        if (count == len(num)):
            i += 1
        numm += 1
    return numm - 1
            


def prime(num):
    if (num == 1):
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if ((num % i) == 0):
            return False
    return True

if __name__ == "__main__":
    print(fun_nth_lefttruncatableprime(25))