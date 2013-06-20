#!/usr/bin/env python3

'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

def sieve(N=None):
    primes = []
    n = 2
    while True:
        yield n
        primes.append(n)
        n += 1
        while any([n % p == 0 for p in primes]):
            n += 1
            if N and n > N:
                raise StopIteration

def main():
    number = 20
    primes = sieve(number)
    result = 1
    for p in primes:
        exp = 1
        while pow(p, exp) <= number:
            exp += 1
        result *= pow(p, exp-1)
    print('Result: ', result)

if __name__ == '__main__':
    main()
