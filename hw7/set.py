#!/usr/bin/env python2
#   set.py (HW7)
#   Author: Chris Kasper
#   Date: 2/23/18
#

def Initialize(A):
    sets = {}
    for i in A:
        sets[i] = i # Inside is the root
    return sets

def Find(s,value):           
    if s[value] != value:
        s[value] = Find(s, s[value])

    return s[value]

def Merge(s, value1, value2):
    # Find the roots of the values
    val1_r = Find(s,value1)
    val2_r = Find(s,value2)

    # Check to make sure not the same set
    if val1_r == val2_r:
        return

    if Size(s,val1_r) > Size(s,val2_r):
        s[val2_r] = val1_r
    else:
        s[val1_r] = val2_r

def Size(s,value):
    # Finds the size of the set
    count = 1
    val_root = Find(s,value)
    for key in s:
        if s[key] == val_root:
            count += 1
    return count
    

def main():
    a = [5,10,11,12,2]
    myset = Initialize(a)

    print myset

if __name__ == '__main__':
	main()

