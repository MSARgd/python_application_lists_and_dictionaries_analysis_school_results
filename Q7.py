#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:38:54 2022

@author: msa
"""
from Data import dic_all_data
from Data import students
from Data import genders
from Data import scores
import numpy as np
import sys
# Q7. Print the name of the student who has the lower mark (of all the DS) in each gender. 

print("gender : ","student : ","lower mark")

for gender in ['M', 'F'] : 
    # selectionner les liste de etudiants(nom,gender) avec leurs notes 
    min_scores_by_gender = list(filter(lambda x: x[2] == gender, zip(students, np.array(scores['DS']).T, genders)))
    min_score = min(min_scores_by_gender, key=lambda x: min(x[1])) # min return the  min array 
    print(gender,"         " ,min_score[0],"       ",min(min_score[1]))
    
    
    
    