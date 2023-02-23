#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:01:55 2022

@author: msa
"""
from Data import dic_all_data
import numpy as np
# Q14. Print the name of the students who progress after each DS.
def get_the_name_of_students_progress_ds() :
    # liste les notes des etudiants
    list_note_std =np.array(dic_all_data['scores']['DS']).T.tolist()
    # print(list_note_std)
    # filter les liste de student have list of notes 🢅
    filtered_list = list(filter(lambda l_notes_std : sorted(l_notes_std) == l_notes_std, list_note_std))
    
    name_std_who_progress_DS = [dic_all_data['students'][list_note_std.index(l)] for l in filtered_list]
    print(name_std_who_progress_DS)
    
get_the_name_of_students_progress_ds()