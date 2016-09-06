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
        return self.arr[0]
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __str__(self):
        pass

class MyStack:
    def __init__(self):
        pass
    def push(self, val):
        pass
    def pop(self):
        pass
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __str__(self):
        pass

## Problem 4

def add_position_iter(lst, number_from=0):
    pass

def add_position_recur(lst, number_from=0):
    pass

def add_position_map(lst, number_from=0):
    pass

## Problem 5

def remove_course(roster, student, course):
    pass

## Problem 6

def copy_remove_course(roster, student, course):
    pass

