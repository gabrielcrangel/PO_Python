# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:30:15 2021

@author: gabri
"""

from pulp import *

model = LpProblem("teste_max",LpMinimize)

x = LpVariable("x", lowBound=0, upBound=10)
y = LpVariable(name='y',lowBound=0,cat='Integer')

model += 3*x + 7*y
model += 2*x + 4*y >=24
model += x + 5*y >=6


status = model.solve()

print (model)

print (value(x))
print (value(y))
print (value(model.objective))

print (LpStatus[status]) 