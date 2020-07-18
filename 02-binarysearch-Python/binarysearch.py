"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(array, value):
    # Your code goes here
    if (value not in array):
        return - 1
    else:
        pos = 0
        for i in array:
            if (i == value):
                return pos
            pos += 1
    pass
