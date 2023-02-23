#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:55:33 2022

@author: msa
"""
# Q2. Print the number of each gender in each group.
def q2() :
    genders  = [   'F'   ,   'F' ,  'M'  ,   'M' ,  'F'  ,    'M'  ,  'F'   ,   'F'  ,  'M'  ,  'M' ]
    groups  = [    3    ,    1  ,   1   ,    3  ,   3   ,     1   ,   2    ,    2   ,   1   ,   3 ,3]    
       
    new_dict = {1: {'F': 0, 'M': 0}, 2: {'F': 0, 'M': 0}, 3: {'F': 0, 'M': 0}}
    
    for gd, gp in zip(genders, groups):
        new_dict[gp][gd] += 1
    
    print(new_dict)
if __name__ == '__main__' :
    q2()