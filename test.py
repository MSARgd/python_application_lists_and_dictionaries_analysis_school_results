#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:57:38 2022

@author: msa
"""
# matrix = [[1, 3, 5], [6, 4, 4], [9, 7, 8]]
# filtered_matrix = list(filter(lambda x: all(y > 3 for y in x), matrix))
# print(filtered_matrix)

from functools import reduce

lst = [[98, 78], [47, 39], [90, 100], [41, 13], [44, 99]]
l = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
result = reduce(lambda x, y: x + y, lst)
result = reduce(lambda a, b: a+b, l)
print(result)
