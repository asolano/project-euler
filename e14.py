#!/usr/bin/env python3

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz(start):
    n = start
    while n is not 1:
        n = int(n*0.5) if n%2==0 else 3*n+1
        yield n

def collatz_len(start, cache):
    length = 1
    for n in collatz(start):
        if n in cache:
            length += cache[n]
            break
        length += 1
    cache[start] = length
    return length, start

def main():
    limit = 1000000
    cache = {}
    result = max(collatz_len(x, cache) for x in range(2, limit))
    print('Result: ', result[1])

if __name__ == '__main__':
    main()
