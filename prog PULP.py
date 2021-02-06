# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:30:12 2021

@author: gabri
"""

from pulp import *

model = LpProblem("teste_max",LpMaximize)

x = LpVariable("x", lowBound=0)
y = LpVariable(name='y', lowBound=0)

model += 5*x + 4*y
model += 6*x + 4*y <=24
model += x + 2*y <=6


status = model.solve()

print (model)

print (value(x))
print (value(y))
print (value(model.objective))

print (LpStatus[status]) 