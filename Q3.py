#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:05:42 2022

@author: msa
"""

import Data
dic_all_data = Data.dic_all_data
min_att = Data.min_att
# Q3. Print the name of students who were absent for Monday seance.


def get_absent_by_day(day):
    for delay, std in zip(dic_all_data['attendance'][day][1], dic_all_data['students']):
        if delay in min_att['Absent']:
            print(std)


get_absent_by_day('Monday')


#  par filter
def get_absent_by_day(day):
    absent_students = filter(lambda x: x[0] in min_att['Absent'], zip(
        dic_all_data['attendance'][day][1], dic_all_data['students']))
    absent_students = list(absent_students)
    print(list(absent_students))
    print(list(map(lambda x: x[1], absent_students)))


get_absent_by_day('Monday')
