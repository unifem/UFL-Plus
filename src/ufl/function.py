#!/usr/bin/env python

"""
Mathematical functions.
"""

__authors__ = "Martin Sandve Alnes"
__date__ = "March 11th 2008"

from base import *

### Functions

class MathFunction(UFLObject):
    def __init__(self, name, argument):
        ufl_assert(is_true_scalar(argument), "Need scalar.")
        self.name     = name
        self.argument = argument
        self.free_indices = tuple()
        self.rank = 0
    
    def operands(self):
        return (self.argument,)
    
    def __repr__(self):
        return "%s(%s)" % (self.name, repr(self.argument))

# functions exposed to the user:

def sqrt(f):
    return MathFunction("sqrt", f)

def exp(f):
    return MathFunction("exp", f)

def ln(f):
    return MathFunction("ln", f)

def cos(f):
    return MathFunction("cos", f)

def sin(f):
    return MathFunction("sin", f)

def floor(f):
    return MathFunction("floor", f)

def ceil(f):
    return MathFunction("ceil", f)

