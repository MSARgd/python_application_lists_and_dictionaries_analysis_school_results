#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:37:01 2022

@author: msa
"""
from Data import students,groups
# Q1. Print the name of members of the group 3.

for stud,grp  in zip(students,groups) :
    if(grp==3) :
        print(stud)