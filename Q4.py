#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:19:23 2022

@author: msa
"""
import numpy as np
import Data
import sys
# Q4. Print the name of students with more than 50 points in all DS.
dic_all_data = Data.dic_all_data


def get_name_of_std_with_more_than_note_inds(note):

    matrix_scores_std_in_ds = dic_all_data['scores']['DS']
    m_t = np.array(matrix_scores_std_in_ds).T
    filtered_list = list(filter(lambda x: all(el > note for el in x), m_t))
    filtered_list = [line.tolist() for line in filtered_list]
    # print(filtered_list)
    m_t = m_t.tolist()
    # print(m_t)
    # m_t.index(filtered_list[2])
    indexes = (m_t.index(line) for line in filtered_list)
    # print(list(indexes))
    print(list(dic_all_data['students'][idx] for idx in indexes))


get_name_of_std_with_more_than_note_inds(30)
