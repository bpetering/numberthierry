# class Odd(object):  # TODO inherit from main module
#     @classmethod
#     def test(cls, n):
#         return n % 2 == 1

import math

def check(n):
    if n < 0:
        n = abs(n)
    return n % 2 == 1
