# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:24:05 2021

@author: gabri
"""

from pulp import *

#Dados do problema
rações = [0,1,2,3,4,5]

custo = {0:0.74,
         1:0.70,
         2:0.83,
         3:0.81,
         4:0.73,
         5:0.75}


minimo = {0:200,   #Carboidrato
          1:180,   #Proteína
          2:150}   #Vitamina


inf_nutri = [[50,60,30,40,20,45], 
             [27,30,40.5,20,30,50],
             [50,80,60,30,20,40]]

#Criar as variaveis de decisão
var = LpVariable.dict("R",(rações),lowBound=0)
print(var)

#Criar o modelo
model = LpProblem("Problema_dieta", LpMinimize)


#Criar a função objetivo
lista_fo=[]

for x in var.keys():
    lista_fo.append(var[x]*custo[x])

model+= lpSum(lista_fo)


#Criar as restrições

lista_rest=[]

for i in minimo.keys():
    for j in rações:
        lista_rest.append(var[j] * inf_nutri[i][j])
    model+= lpSum(lista_rest) >= minimo[i]
    lista_rest=[]

print(model)

#Solução do modelo


status = model.solve()

print(LpStatus[status])

print(" ")

print(f'O custo mínimo é de R${value(model.objective)}')

for x in var.values():
    if value(x) != 0:
        print(f'{x} = {value(x)} ')
    else:
        continue
    
