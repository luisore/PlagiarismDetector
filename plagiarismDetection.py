# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:49:57 2024

@author: ricar
"""
from difflib import SequenceMatcher

with open('demo1.txt') as one_file , open('demo2.txt') as two_file:
    data_file1 = one_file.read()
    data_file2 = two_file.read()
    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    print(f'The plagiarized content is {matches*100}%')