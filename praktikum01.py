# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 07:55:36 2020

@author: LENOVO i5
"""

baris = 10
kolom = baris

for i in range(baris):
    for j in range(kolom):
        tambahkan = i+j
        print("{0:>5}".format(tambahkan),end='')
    print()
    
    