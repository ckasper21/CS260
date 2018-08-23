#!/usr/bin/python
# HW 2 - problem 3 (timeit)
# Author: Chris Kasper

import timeit
from problem1 import *
from problem2 import *

setup_fib = """
from __main__ import n
from problem1 import fib
"""

setup_fibmemo = """
from __main__ import n
from problem2 import fib_memo, memo
"""

def main():

    file = open("data.out",'w')
    ## file.write("n          fib(n) (s)           fib_memo(n) (s)\n")
    
    global n
    for n in range(1,41):
        time_fib = timeit.timeit('fib(n)', setup=setup_fib, number=1)
        time_fibmemo = timeit.timeit('fib_memo(n)', setup=setup_fibmemo, number=1)
        clear_memo()
        file.write(str(n)+" "+str(time_fib)+" "+str(time_fibmemo)+'\n')
    file.close()

if __name__ == '__main__':
    main()
