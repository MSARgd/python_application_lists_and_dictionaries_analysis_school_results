#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 13:00:52 2022

@author: msa
"""
from Data import dic_all_data
import numpy as np
import sys
from functools import reduce
from statistics import median
# # Q16. Print the Finale_note for each student.
#  * Finale_note = (Mean_of_DS *.6 + Mean_of_TPs * 0.15 + Median_of_group_DS * 0.25) * Attendance_rate

notes_std_in_ds =np.array(dic_all_data['scores']['DS']).T
notes_std_in_tp =np.array(dic_all_data['scores']['TP']).T
# Mean_of_DS 80.6
list_mean_std_in_ds = list(map(lambda l : l.mean()*0.6,notes_std_in_ds))
# Mean_of_TPs *0.15
list_mean_std_in_tp = list(map(lambda l : l.mean()*0.15,notes_std_in_tp))
# Median_of_group_DS
    # convertire la liste des liste à un seul liste
reduced_list_note_in_one_list= reduce(lambda l,next_l : l+next_l,dic_all_data['scores']['DS'])
Median_of_group_DS = median(reduced_list_note_in_one_list)
# print(Median_of_group_DS)
# -----------------------------------------------------

matrix = np.zeros((10,4)) #matrice de 10 linge et 4 colomun (pour le regroupement du attendans des e
# etudiants (chaque line correspond aux attendance de etudiant))
# print(matrix)
i=0
total_attendace =0
for l in dic_all_data['attendance'].values() :
    total_attendace += l[0]
    line = np.array(list(map(lambda x: l[0]-x,l[1])))
    matrix[:,i] = line
    i=i+1
# -----------------------------------------------------------------
list_attendans_std=[]
for line in matrix.tolist() :
    list_attendans_std.append(sum(line)/total_attendace)
# print(list_attendans_std)
print("Nom :   Finale Note ")
for name_std,Mean_of_DS_0_6,Mean_of_TPs_0_15,Attendance_rate in zip(dic_all_data['students'],list_mean_std_in_ds,list_mean_std_in_tp,list_attendans_std) :
    Finale_note = (Mean_of_DS_0_6 + Mean_of_TPs_0_15 +Median_of_group_DS * 0.25)*Attendance_rate
    print("{}   {} ".format(name_std,Finale_note))