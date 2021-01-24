# -*- coding: utf-8 -*-

"""
Gaia Cervini
Exercise 3.2
Jan 24 2021
"""

def do_twice(func, arg):
    func(arg)
    func(arg)


def print_twice(arg):
    print(arg)
    print(arg)
    

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

    
    
if __name__ == '__main__':

   do_twice(print,'spam')
   
   do_twice(print_twice,'spam')
   
   do_four(print_twice,'spam')
