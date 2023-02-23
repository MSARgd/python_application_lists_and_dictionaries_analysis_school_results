#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 10:51:29 2022

@author: msa
"""
import sys
# Q13. Print the name of the Male student in group 1 with the highest note in the second DS.
from Data import dic_all_data,genders,groups
def get_name_of_the_male_std_satisfaild_contraints_of_q3() :
    # cette liste regroupe le etudiant avect leurs gender,group,score in the   the second DS
    l_grouped_name_gender_note = list(zip(dic_all_data['students'],genders,groups,dic_all_data['scores']['DS'][1]))
    # print(l_grouped_name_gender_note)
    filtred_list = list(filter(lambda tuple_: tuple_[1]=='M' and tuple_[2]==1  , l_grouped_name_gender_note))
    # print(filtred_list)
    std = max(filtred_list,key= lambda x : x[3])
    # print(std)
    print(std[0])


get_name_of_the_male_std_satisfaild_contraints_of_q3()