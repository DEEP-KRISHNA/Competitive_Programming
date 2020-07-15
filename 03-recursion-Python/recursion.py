"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if (position == 1):
        return 1
    elif (position == 2):
        return 1
    elif (position == 0):
        return 0
    else:
        return get_fib(position-1) + get_fib(position-2)
    # return -1

if __name__ == "__main__":
    print(get_fib(0))