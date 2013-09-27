#!/usr/bin/env python3

'''
A Pythagorean triple is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

def make_triplet(limit):
    for a in range(1, limit):
        for b in range(a+1, limit):
            c = pow(a*a + b*b, 0.5)
            if c == int(c):
                yield a, b, int(c)

def main():
    limit = 1000
    result = None
    for a, b, c in make_triplet(limit):
        if a + b + c == limit:
            result = a * b * c
            break
    print('Result: ', result)

if __name__ == '__main__':
    main()
