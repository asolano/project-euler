#!/usr/bin/env python3

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

def main():
    exp = 1000
    result = sum((int(c) for c in str(pow(2,exp))))
    print('Result: ', result)

if __name__ == '__main__':
    main()
