#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:39:53 2022

@author: msa
"""
from Data import dic_all_data,students
# Q15. Print the name of the student with the highest number of attendance for both Monday & Friday seances.
def get_name_most_late_std_in_monday_friday() :
    for day in ['Monday','Friday'] :    
        idx_student = dic_all_data['attendance'][day][1].index(max(dic_all_data['attendance'][day][1]))
        print(students[idx_student])
get_name_most_late_std_in_monday_friday()