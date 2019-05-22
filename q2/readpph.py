import pandas as pd
import numpy as np
import os.path
import re
import math
import CPUtimer
from sys import argv

##############################################################################3
#Importar Arquivo de entrada
with open("pph_100_01.dat") as f: # Abre, lê e fecha o arquivo de entrada
    texto = f.readlines()

#Converte dados de entrada ai e bi de txt em integer
def convert(ini,fim):
    lista = [ ]
    for i in range(ini,fim):
        z1 = texto[i]
        z1a = z1.split(" ")
        z1a.remove('')
        z1b=z1a.pop()
        z1c = re.sub(r"\n", "", z1b)
        z1a.append(z1c)
        z1d = [int(val) for val in z1a]
        lista.extend(z1d)
    return lista

##############################################################################
# Define,converte e inicia variáveis de entrada
def getData():
    a2 = [ ]
    b2 = [ ]
    z0 = texto[0]
    z0 = int(z0)
    n = math.ceil(z0/10)
    L = 0
    x = [ ]
    arm = 0
    t = 0

    # Converte os valores a0 e b0 em integer
    a0 = texto[n+1]
    a0 = int(a0)
    b0 = texto[2*n+2]
    b0 = int(b0)
    abi = [ ]#exc
    # Converte os valores de ai e bi em integer
    ai = convert(1,n+1)
    bi = convert(n+2,2*n+2)

    # Retira valor 0 do denominador
    for w in range(0,z0): 
        if bi[w] == 0:
            bi[w] = 1
    #print (ai) #exc
    #print (bi) #exc
    for i in range(z0):#exc
        abi.insert(i,ai[i]/bi[i])#exc
    #print (abi)#exc
    # Zera vetor que indica os valores inseridos no somatório
    for i in range(1,z0+1): 
        x.insert(i,0)

    # Inicia Variáveis
    sa = a0 # sa = somatório de a
    sb = b0 # sb = somatório de b
    #print (sa)
    #print (sb)
    sab = sa/sb#exc
    print(len(ai))
    print(len(bi))
    print (sab)#exc

    return ai,bi,abi,a0,b0 
