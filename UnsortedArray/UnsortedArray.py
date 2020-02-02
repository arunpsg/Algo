def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        print("Enter valid inputs")
        return None
    min = max = ints[0]

    for input in ints:
        if min > input:
            min = input
        if max < input:
            max = input
    return min, max
    pass


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 0)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if (None == get_min_max(l)) else "Fail")
