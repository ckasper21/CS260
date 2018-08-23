#!/usr/bin/env python2
#   make_heap.py (HW5)
#   Author: Chris Kasper
#   Date: 2/9/18
#

import timeit
import random

def make_heap(x):
    for i in range((len(x)/2)+1,-1,-1):
        downheap(x,i)

def downheap(H,i):
    while (2*i+1) < len(H):
        lgi = 2*i+1

        try:
            if ((2*i+2) <= len(H)) and (H[lgi] < H[2*i+2]):
                lgi = 2*i+2
        except IndexError:
            None

        if H[i] < H[lgi]:
            tmp = H[i]
            H[i] = H[lgi]
            H[lgi] = tmp
            i = lgi
        else:
            return

setup_heap = """
from __main__ import H, make_heap
"""

# Test set I originally used
H_data = [[8,5,2],[8,5,2,9],[8,5,2,9,1],[8,5,2,9,1,10],[8,5,2,9,1,10,7],[8,5,2,9,1,10,7,6],[8,5,2,9,1,10,7,6,11],
            [8,5,2,9,1,10,7,6,11,22],[8,5,2,9,1,10,7,6,11,22,26],[8,5,2,9,1,10,7,6,11,22,26,19]]


def main():

    global i, H
    
    print("n     makeheap(n)")
    for i in range(1000,50001,1000):
        H = range(0,i)
        random.shuffle(H)
        time_heap = timeit.timeit('make_heap(H)', setup=setup_heap, number=1)
        print(str(i)+"  "+str(time_heap));


if __name__ == '__main__':
	main()
