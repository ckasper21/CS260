#!/usr/bin/python
# HW 2 - problem 1 (list_concat)
# Author: Chris Kasper

import sys
from cell import *

def list_concat(A,B):
    # Connect A.next's last element to the beginning of B
    end = A
    while end.next is not None:
        end = end.next
    end.next = B
    return A

def main():
    x = Cell( 13 )
    y = Cell(15,x)
    a = Cell( 1 )
    b = Cell(2,a)

    print "x is holding: " + list2string( x )
    print "y is holding: " + list2string( y )
    print "a is holding: " + list2string( a )
    print "b is holding: " + list2string( b )

    test1 = list_concat(b,y)
    print "list_concat(b,y) returns: " + list2string(test1)

if __name__ == '__main__':
	main()
