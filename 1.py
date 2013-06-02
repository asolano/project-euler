#!/usr/bin/env python3

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
'''

def main():
    # Direct approach
    #result = sum([x if not(x%3) or not(x%5) else 0 for x in range(1000)])
    result = sum([0 if x%3 and x%5 else x for x in range(1000)])
    print('Result: ', result)

if __name__ == '__main__':
    main()
