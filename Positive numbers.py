# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Python programme that takes string as input and arrange letters in decreasing order of frequency

W= input('Please enter a string ')

def most_frequent(string):
    
    d = dict()
    
    for key in string:
        
        if key not in d:
            
            d[key] = 1
            
        else:
            
            d[key] += 1
            
    return 

print (most_frequent(W))
