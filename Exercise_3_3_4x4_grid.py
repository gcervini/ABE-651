# -*- coding: utf-8 -*-

"""
Gaia Cervini
Exercise 3.3
Jan 24 2021
"""

def chunk1():
    print('+ - - - -', end=' ')


def first_line():
    do_four(chunk1)
    print('+')
    
    
def chunk2():
    print('|        ', end=' ')
    
    
    
def second_line():
    do_four(chunk2)
    print('|')
    
    
def do_four(func):
    func()
    func()
    func()
    func()
    
def row():
    first_line()
    do_four(second_line)
    

def print_grid():
    do_four(row)
    first_line()
    
    
if __name__ == '__main__':

   
    print_grid()
