#!/usr/bin/env python3

'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import itertools

def is_palindrome(n):
    word = str(n)
    half = int(len(word)/2)
    a = itertools.islice(word, 0, half)
    b = itertools.islice(reversed(word), 0, half)
    return all(x == y for x, y in zip(a, b))

def main():
    high = 999
    low = 99
    result = 0
    for x, y in itertools.product(range(high, low, -1), range(high, low, -1)):
        # Ignore already seen pairs
        if x < y:
            continue
        mul = x * y
        # Skip smaller products
        if mul < result:
            continue
        if is_palindrome(mul):
            result = max(mul, result)
    print('Result: ', result)

if __name__ == '__main__':
    main()
