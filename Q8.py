#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 16:11:14 2022
@author: msa
"""

# Q8. Print the mean mark of TPs for each gender.
from Data import dic_all_data
from Data import genders
import numpy as np
import sys
from functools import reduce
def get_mean_mark_of_tp_each_gender() :
    print("gender : ","mean mark : ")
    for gender in ['M','F'] :
        # selectionner les liste de notes
        score_tp_by_gender = list(filter(lambda x : x[1]==gender, zip(np.array(dic_all_data['scores']['TP']).T.tolist(),genders)))  
        l_scores = list(map(lambda x : x[0],score_tp_by_gender))
        # print(l_scores)
        # la 1er reduce va convertire  la list des listes à  une lite des entier (+ : concatenation)
        s=reduce(lambda x,y : x+y ,reduce(lambda x,y: x + y, l_scores)) 
        print(gender,"        ",s/(len(l_scores)*2))
   

get_mean_mark_of_tp_each_gender()
  


