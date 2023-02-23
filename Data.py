#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:10:39 2022

@author: msa
"""

#Data
students= ['Sara', 'Zineb', 'Mohamed', 'Ali', 'Khadija', 'Idriss', 'Najat', 'Nadia', 'Marouane', 'Ahmed']
#---------------------------------------------------------------------------------------------------
genders  = [   'F'   ,   'F' ,  'M'  ,   'M' ,  'F'  ,    'M'  ,  'F'   ,   'F'  ,  'M'  ,  'M' ]
groups  = [    3    ,    1  ,   1   ,    3  ,   3   ,     1   ,   2    ,    2   ,   1   ,   3 ]
regions=['S','C','N']

#---------------------------------------------------------------------------------------------------
#scores   = {'DS': length of DS is the number of DS
#                  The element of each DS is the mark of each student
#           'TP': length of TP is the number of TP
#                  The element of each TP is the mark of each student
scores   = {'DS' : [[36, 58, 46, 96, 9, 82, 83, 66, 35, 47],
                   [46, 50, 55, 21, 22, 76, 51, 90, 96, 48],
                   [56, 54, 53, 17, 31, 74, 11, 53, 98, 67],
                   [77, 38, 8, 74, 39, 39, 52, 66, 38, 86],
                   [93, 21, 7, 33, 10, 97, 48, 96, 24, 7],
                   [97, 98, 95, 75, 64, 9, 48, 51, 45, 82]],

           'TP': [[48, 63, 98, 47, 25, 90, 100, 21, 41, 44],
                  [73, 79, 78, 39, 11, 100, 57, 96, 13, 99]]}
#---------------------------------------------------------------------------------------------------
# attendance = { Day : [ Duration_session : [ delay of 10 sessions]]}
attendance = {'Monday'    : [60, [3, 31, 1, 56, 15, 49, 48, 20, 2, 38]],
              'Tuesday'   : [120,[8, 3, 2, 7, 5, 9, 4, 0, 6, 1]],
              'Wednesday' : [60, [2, 7, 14, 6, 9, 15, 12, 13, 10, 0]],
              'Friday'    : [120,[12, 50, 0, 15, 11, 10, 3, 6, 14, 2]]}
#---------------------------------------------------------------------------------------------------
# min_att = {Attendance_statut : Late_Minute}
min_att = {'Present': range(0,1,1), 'Late' : range(1,6,1), 'Very Late': range(6,15,1), 'Absent': range(15,180,1)} 
# dic_att = { Attendance_statut : rate}
dic_att = {'Present': 1.0, 'Late': 0.97, 'Very Late': 0.93, 'Absent': 0.9} 
dic_all_data={'students':students,'scores':scores,'attendance':attendance}