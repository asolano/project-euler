#!/usr/bin/env python3

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
'''

import itertools
import collections
import math

def is_prime(n):
    """
    Return True if n is prime. Uses trial division.

    NOTE: All primes greater than 3 can be expressed as 6k+1 or 6k-1
    """
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    k = 1
    sqrt_n = math.floor(math.sqrt(n))
    while True:
        c1 = 6 * k - 1
        c2 = 6 * k + 1
        if n == c1 or n == c2:
            return True
        if n % c1 == 0 or n % c2 == 0:
            return False
        if c2 > sqrt_n:
            break
        k += 1
    return True

def main():
    number = 10001
    primes = (x for x in itertools.count() if is_prime(x))
    it = itertools.islice(primes, number-1, number)
    print('Result:', list(it)[0])

if __name__ == '__main__':
    main()
