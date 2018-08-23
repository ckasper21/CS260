#!/usr/bin/python
# HW 2 - problem 1 (list_concat)
# Author: Chris Kasper

import sys
import timeit
from cell import *
from problem1 import *
from problem2 import *

def makelist1(num):
    # Makes a list of odd numbers
    x=1
    rv_ls = Cell(x)
    x+=2
    count = 0
    cell = rv_ls
    while count < num:
        cell.next = Cell(x)
        cell = cell.next
        count+=1
        x+=2

    return rv_ls

def makelist2(num):
    # Makes a list of even numbers
    x=0
    rv_ls = Cell(x)
    x+=2
    count = 0
    cell = rv_ls
    while count < num:
        cell.next = Cell(x)
        cell = cell.next
        count+=1
        x+=2

    return rv_ls

file = open("data.out",'w')
file.write("Used timeit to time the two functions created for list\n\n")
file.write("length          list_concat (s)           list_concat_copy (s)\n")
file.write("----------------------------------------------------------\n")
for i in range(1000,16000,1000):
    list1=makelist1(i)
    list2=makelist2(i)

    mytime_concat = timeit.Timer('list_concat(list1,list2)','from problem1 import list_concat\n'+
                'from __main__ import list1, list2')
    delta_concat = mytime_concat.timeit(1)

    mytime_concat_copy = timeit.Timer('list_concat(makelist1(10000),makelist2(10000))','from problem2 import list_concat_copy\n'+
                'from __main__ import makelist1, makelist2')
    delta_concat_copy = mytime_concat.timeit(1)

    file.write(str(i)+"         "+str(delta_concat)+"         "+str(delta_concat_copy)+'\n')

file.close()
