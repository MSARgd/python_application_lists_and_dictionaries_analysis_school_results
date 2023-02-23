#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:40:09 2022
@author: msa
"""
# Q10. Print the name of  the student with a mean mark more than 80 in all TPs and an Attendance Rate more than 0.95.
from Data import dic_all_data
import numpy as np
import sys
from functools import reduce
#  method tolist convert matrix to list of listes
# ======================================contrainte 1==================================

m_t = np.array(dic_all_data['scores']['TP']).T.tolist()

std_scores_tp = list(zip(dic_all_data['students'],m_t))

filters_std_scores_tp = list(filter(lambda el : sum(el[1])/len(el[1]) > 80 ,std_scores_tp))
l_index_std_valid_contarint_1= list(map(lambda x: dic_all_data['students'].index(x[0]) ,filters_std_scores_tp))
# print(l_index_std_valid_contarint_1)
# ======================================(contrainte 2(result Contrainte_1)==================================

for idx in l_index_std_valid_contarint_1 :    
    s_dif,t_durations =0,0
    for el in  list(dic_all_data['attendance'].values()) :
        s_dif += el[0] - el[1][idx]
        t_durations += el[0]
    if(s_dif/t_durations > 0.95) :
        print(s_dif/t_durations)
        print(dic_all_data['students'][idx])


