#!/usr/bin/env python
#   post.py (HW4)
#   Author: Chris Kasper
#   Date: 2/2/18
#

import sys
import operator
from lexer import *

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftc = None
        self.rightc = None

    def add_child(self, obj,num):
        if num == 0:
            self.leftc = obj
        else:
            self.rightc = obj

def prefix(T):
    if not T:
        exit(1)
    else:
        print T.data ,
        if T.leftc != None:
            prefix(T.leftc)
        if T.rightc != None:
            prefix(T.rightc)

def postfix(T):
    if not T:
        exit(1)
    else:
        if T.leftc != None:
            prefix(T.leftc)
        if T.rightc != None:
            prefix(T.rightc)
        print T.data ,

def infix(T):
    if not T:
        exit(1)
    else:
        if T.leftc != None:
            prefix(T.leftc)
        print T.data ,
        if T.rightc != None:
            prefix(T.rightc)

def evalexp(T):
    Op = operator
    if not T:
        exit(1)
    else:
        if str.isdigit(T.data):
            return int(T.data)
        else:
            operand = T.data
            if T.leftc != None:
                op1 = evalexp(T.leftc)
            if T.rightc != None:
                op2 = evalexp(T.rightc)
            if operand == "+":
                return Op.add(op1,op2)
            elif operand == "-":
                return Op.sub(op1,op2)
            elif operand == "*":
                return Op.mul(op1,op2)
            elif operand == "/":
                return Op.div(op1,op2)

while get_expression():
	t = get_next_token()
        stack = []
	while t:
		if str.isdigit( t[0] ) : # we have a (non-negative) number
                        stack.append(Node(t))
		else:
                    sec_op = stack.pop()
                    fir_op = stack.pop()
                    Oper = Node(t)
                    Oper.add_child(sec_op,1)
                    Oper.add_child(fir_op,0)
                    stack.append(Oper)
                        
		t = get_next_token()

        print "pre: ",
        prefix(stack[0])
        print "\nin: ",
        infix(stack[0])
        print "\npost: ",
        postfix(stack[0])
        print "\neval: ",
        print(evalexp(stack[0]))
        print "\n"
