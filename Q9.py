#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 18:16:28 2022
@author: msa
"""
# Q9. Print the name of the student who has the lower minutes of delay in all seances.
from Data import dic_all_data
import sys
# 
def print_name_std_has_lower_delay_by_seances() :
    print("seance : name student  :  lower delay ")
    for key in  dic_all_data['attendance'].keys() :
        list_delay_by_std = list(zip(dic_all_data['attendance'][key][1],dic_all_data['students']))
        list_delay_by_std = list(zip(dic_all_data['attendance'][key][1],dic_all_data['students']))
        
        tuple_min_delay_std = min(list_delay_by_std,key=lambda x : x[0]) # min ici elle retourne le tuple qui a le minimum delay
        print("{}     {}         {}".format(key,tuple_min_delay_std[1],tuple_min_delay_std[0]))
    
print_name_std_has_lower_delay_by_seances()






