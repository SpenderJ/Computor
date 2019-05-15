# imports
from math import sqrt


def prime_check(n):
    a = 2
    if n == a: return True
    elif n < a: return False
    else:
        while a <= int( sqrt(n) ) + 1:
            if n % a == 0:
                return False
            else:
                a += 1
        else:
            return True


def factorial(n):
    if n > 1: return factorial(n - 1) * n
    else: return 1