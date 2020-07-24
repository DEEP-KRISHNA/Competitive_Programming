# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def fun_nearestkaprekarnumber(n):
    num1 = n
    num2 = n
    while (not check(num1)):
        num1 += 1
    while (not check(num2)):
        num2 -= 1
    if (n - num2 > num1 - n):
        return num1
    return num2

def check(num):
    poww = num * num
    poww = str(poww)
    for j in range(1, len(poww)):
        left = poww[:j]
        right = int(poww[j:])
        if (right != 0):
            if ((int(left) + right) == num):
                return True
    return False

if __name__ == "__main__":
    print(fun_nearestkaprekarnumber(49))
