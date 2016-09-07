##### Filename: util.py
##### Author: Billie Wei
##### Date: September 6, 2016
##### Email: billiewei@college.harvard.edu

import copy
from collections import deque

## Problem 1

# Helper function to make a column from y's rows
def columnfy(y, column):
    arr = []
    for i in range(len(y)):
        arr.append(y[i][column])
    return arr

# Function to multiple a row from x and column from y
def do_mult(x, y):
    total = 0
    for column in range(len(y)):
        total = total + x[column]*y[column]
    return total

def matrix_multiply(x, y):
    # Initialize storage array of proper size, filled with zeroes
    arr = [[0 for columns in range(len(y[0]))] for rows in range(len(x))]
    for row in range(len(x)):
        for col in range(len(y[0])):
            arr[row][col] = do_mult(x[row], columnfy(y, col));
    return arr
        
## Problem 2, 3

class MyQueue:
    arr = []
    def __init__(self):
        self
    def push(self, val):
        self.arr.append(val)
    def pop(self): 
        if len(self.arr) < 1:
            return None
        return_value = self.arr[0]
        del self.arr[0]
        return return_value
    def __eq__(self, other):
        if len(self.arr) != len(other):
            return False
        else:
            for i in range(len(self.arr)):
                if self.arr[i] != other[i]:
                    return False
            return True
    def __ne__(self, other):
        if len(self.arr) != len(other):
            return True
        else:
            for i in range(len(self.arr)):
                if self.arr[i] != other[i]:
                    return True
            return False
    def __str__(self):
       print "PRINTING SELF!"
       a = map(str, self.arr)
       print ', '.join(a)
       return ', '.join(a)

class MyStack:
    arr = []
    def __init__(self):
        self
    def push(self, val):
        self.arr.append(val)
        print self.arr
    def pop(self):
        if len(self.arr) < 1:
            return None
        return_value = self.arr[len(self.arr)-1]
        del self.arr[len(self.arr)-1]
        return return_value
    def __eq__(self, other):
        if len(self.arr) != len(other):
            return False
        else:
            for i in range(len(self.arr)):
                if self.arr[i] != other[i]:
                    return False
            return True
    def __ne__(self, other):
        if len(self.arr) != len(other):
            return True
        else:
            for i in range(len(self.arr)):
                if self.arr[i] != other[i]:
                    return True
            return False
    def __str__(self):
        print "PRINTING SELF!"
        a = map(str, self.arr)    
        print ', '.join(a)
        return ', '.join(a)

## Problem 4

def add_position_iter(lst, number_from=0):
    arr = []
    for i in range(len(lst)):
        arr.append(lst[i]+i+number_from)
    #print "This is my array:"
    #print arr
    return arr

def add_position_recur(lst, number_from=0):
    arr = []
    return arr

def add_position_map(lst, number_from=0):
    arr = list(map(lambda x: x+number_from+lst.index(x),lst))
    return arr

## Problem 5

def remove_course(roster, student, course):
    pass

## Problem 6

def copy_remove_course(roster, student, course):
    pass

