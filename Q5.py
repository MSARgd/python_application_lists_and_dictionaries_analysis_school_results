#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 21:32:40 2022

@author: msa
"""

import numpy as np
import Data
dic_all_data = Data.dic_all_data
groups = Data.groups
# Q5. Print the mean mark (DS) of all student of each group.


def get_mean_mark_ds_of_all_std_by_gp():
    matrix_scores_std_in_ds = dic_all_data['scores']['DS']
    m_t = np.array(matrix_scores_std_in_ds).T
    means = list([line.mean() for line in m_t])
    # print(means)
    dict_mean_by_gp = {1: {'mean': []}, 2: {'mean': []}, 3: {'mean': []}}
    for gp, mean in zip(groups, means):
        dict_mean_by_gp[gp]['mean'].append(mean)
    for el in dict_mean_by_gp:
        # print (sum(dict_mean_by_gp[el]['mean'])/len(dict_mean_by_gp[el]['mean']))
        dict_mean_by_gp[el]['mean'] = sum(
            dict_mean_by_gp[el]['mean'])/len(dict_mean_by_gp[el]['mean'])

    print(dict_mean_by_gp)


get_mean_mark_ds_of_all_std_by_gp()
