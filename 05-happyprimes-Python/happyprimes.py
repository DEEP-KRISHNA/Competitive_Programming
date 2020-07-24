# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
import math

def ishappyprimenumber(n):
    # Your code goes here
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    print("prime")
    return happy(n)
    # pass

def happy(n):
    if(n<10):
        if (n == 1 or n == 7):
            return True
        else:
            return False
    else:
        n = str(n)
        summ = 0
        for i in n:
            summ = summ + (int(i) ** 2)
        # print(summ)
        return happy(summ)

if __name__ == "__main__":
    ishappyprimenumber(833)
