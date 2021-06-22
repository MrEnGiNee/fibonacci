# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# python programme for fibonacci numbers

def fibonacci(n):
    
    # check if input is 0 then it will
    # print incorrect input
    
    if n<0:
        print("Incorrect input")
        # check if n is 0
        # then it will return 0
        
        elif n==0:
            return 0
        
        # check if n is 1,2
        # it will return 1
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

