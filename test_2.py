#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 09:24:17 2019

@author: kostya
"""
import numpy as np



'''
# Homogeneous equations
hom_eq = np.array([[0, 10, 4, -2],
                   [-3, -17, 1, 2],
                   [1, 1, 1, 0], 
                   [8, -34, 16, -10]])
print(hom_eq.shape)
# Coefficiens
const_eq = np.array([-4, 2, 6, 4])
const_eq_0 = np.array([0, 0, 0, 0])
print(const_eq.shape)

aug_matr = np.column_stack((hom_eq, const_eq))
print(aug_matr, '\n', aug_matr.shape)
columns_name = ['x1', 'x2', 'x3', 'x4']
x = np.linalg.solve(hom_eq, const_eq)
print(np.allclose(np.dot(hom_eq, x), const_eq))
'''
