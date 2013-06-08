#!/usr/bin/env python3

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def prime_factors(N):
    i = 2
    while i <= N:
        if N % i == 0:
            N /= i
            yield i
        else:
            i += 1

def main():
    number = 600851475143
    result = max(prime_factors(number))
    print('Result: ', result)

if __name__ == '__main__':
    main()
