#!/usr/bin/python
# HW 2 - problem 2 (list_concat_copy)
# Author: Chris Kasper

import sys
from cell import *

def list_concat_copy(A,B):
    nlist = Cell(A.data)
    cell = nlist

    while A.next is not None:
        cell.next = Cell(A.next.data)
        cell = cell.next
        A = A.next

    cell.next = Cell(B.data)
    cell = cell.next

    while B.next is not None:
        cell.next = Cell(B.next.data)
        cell = cell.next
        B = B.next

    return nlist

def main():
    x = Cell( 13 )
    y = Cell(15,x)
    a = Cell( 1 )
    b = Cell(2,a)

    print "x is holding: " + list2string( x )
    print "y is holding: " + list2string( y )
    print "a is holding: " + list2string( a )
    print "b is holding: " + list2string( b )

    test2 = list_concat_copy(b,y)
    print "list_concat_copy(b,y) returns: " + list2string(test2)

if __name__ == '__main__':
	main()
