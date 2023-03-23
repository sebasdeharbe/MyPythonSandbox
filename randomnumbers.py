#Random Numbers!
from ctypes import sizeof
from random import seed
from random import random
from math import pow
seed(10)

lista = []

for i in range(1000000):
    lista.append(round(random()*100000000000))

for i in lista:
    print(i)

