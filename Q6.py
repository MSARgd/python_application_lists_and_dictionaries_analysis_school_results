#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:34:56 2022

@author: msa
"""
# Q6. Print the seance for each group with less delay in min.

import Data
attendance = Data.attendance
groups = Data.groups

# ----------------------------
print('group :',end='  ')
print('Duration_session :',end='     ')
print('day :  ',end='  ')
print('delay :  ')

for day, session_info in attendance.items():
    duration = session_info[0]
    delays = session_info[1]
    for i in range(len(groups)):
        print(groups[i],end='              ')
        print(duration,end='         ')
        print(day,end='         ')
        print(delays[i])

