# -*- coding: utf-8 -*-

"""
Gaia Cervini
Exercise 3.3
Jan 24 2021
"""

def do_twice(func, arg):
    func(arg)
    func(arg)


def print_twice(arg,arg2=' '):
    print(arg, end=arg2)
    print(arg, end=arg2)
    

def do_four(func, arg=None):
    do_twice(func, arg)
    do_twice(func, arg)

    
def print_mainline():
    print('+',end=' ')
    do_twice(print_twice, '-') 
    print('+',end=' ')
    do_twice(print_twice, '-')
    print('+',end='\n')
    
    
def print_secondline(arg=None):
    print('|',end=' ')
    do_twice(print_twice,' ')
    print('|',end=' ')
    do_twice(print_twice,' ')
    print('|',end='\n')
    

def print_grid():
    print_mainline()
    do_four(print_secondline)
    print_mainline()
    do_four(print_secondline)
    print_mainline()
    
    
if __name__ == '__main__':

    print_grid()
    

    

