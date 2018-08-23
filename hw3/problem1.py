#!/usr/bin/python
# HW 3 - problem 1 ()
# Author: Chris Kasper

import sys

def fib(num):
    if num == 0: # per hw spec Fib(0)=1
        return 1
    elif num == 1: # per hw spec Fib(1)=1
        return 1
    else:
        return fib(num-1) + fib(num-2)

def main():
    ans = fib(int(sys.argv[1]))
    print(ans)

if __name__ == '__main__':
	main()
