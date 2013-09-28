#!/usr/bin/env python3

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

def sieve(N):
    primes = [True for _ in range(2, N+1)]
    sqroot = int(pow(N, 0.5))
    for i in range(2, sqroot+1):
        if primes[i-2]:
            for j in range(i*i, N+1, i):
                primes[j-2] = False
    return [i+2 for i,x in enumerate(primes) if x]

def main():
    limit = 2000000
    result = sum(sieve(limit))
    print('Result: ', result)

if __name__ == '__main__':
    main()
