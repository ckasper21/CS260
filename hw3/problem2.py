#!/usr/bin/python
# HW 3 - problem 2 ()
# Author: Chris Kasper

import sys

memo = [None]*101
memo[0] = 1
memo[1] = 1

def fib_memo(num):
    if num in memo:
        return memo[num]
    elif num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        value = fib_memo(num-1) + fib_memo(num-2)
        memo[num] = value
        return value

def clear_memo():
    global memo 
    memo = [None]*101
    memo[0] = 1
    memo[1] = 1

def main():
    ans = fib_memo(int(sys.argv[1]))
    clear_memo()
    print(ans)

if __name__ == '__main__':
	main()
