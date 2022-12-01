# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:29:35 2022

@author: rcpat
"""


#%% Part 1
with open("adventofcode\\advent-of-code\\2022\\input_files\\day1.txt", 'r') as file:
    data = file.read().split('\n\n')
    data2 = [[int(item) for item in pack.splitlines()] for pack in data]
    result = max([sum(l) for l in data2])
    
#%% Part 2
with open("adventofcode\\advent-of-code\\2022\\input_files\\day1.txt", 'r') as file:
    data = file.read().split('\n\n')
    data2 = [[int(item) for item in pack.splitlines()] for pack in data]
    result = sum(sorted([sum(l) for l in data2], reverse = True)[:3])