#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    return some_int % 100000000


def optimized_fibonacci(f):
    """
    Returns the fth Fibonacci number.
    """
    
    if f < 0:
        raise ValueError("Input must be non-negative.")
    elif type(f) is not int:
        raise ValueError("Input must be a natural number.")

    f_0 = 0
    f_1 = 1
    if f == 0:
        return f_0
    elif f == 1:
        return f_1
    else:
        f_m = 0
        f_n = 1
        for i in range(f-1):
            # add up the last two numbers
            m = f_n
            f_n = f_m + f_n
            f_m = m
        return f_n


class SummableSequence(object):
    def __init__(self, *initial):
        SummableSequence.sequence = list(initial)

    def __call__(self, i):
        n = len(self.sequence)
        for k in range(i):
            self.sequence.append(sum(self.sequence[-n:]))
        return self.sequence[-1]


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))
    

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
