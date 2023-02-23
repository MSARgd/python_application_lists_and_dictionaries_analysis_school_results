#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 00:51:38 2022

@author: msa
"""
 # Print the name of the student who has the higher minutes of delay in the third seance.
from Data import dic_all_data
def get_the_std_has_higher_delay_in_seance_x(seance) :
    l = list(zip(dic_all_data['students'],dic_all_data['attendance'][seance][1]))
    higher_delay_relased_by = max(l,key=lambda x : x[1])
    print(higher_delay_relased_by[0])

 # in the third seance => Wednesday
get_the_std_has_higher_delay_in_seance_x('Wednesday')