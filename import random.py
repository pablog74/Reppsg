'''
from random import randint

lista= [randint(1, 100)for _ in range(100)]  

print (lista)
'''
lista=[1, 5, 6, 2, 99, 14, 91, 65, 7, 9]

for i in range(0, len(lista)-1):
    for j in range (0, len (lista)-i-1):
        if (lista[j] > lista[j+1]) :
            lista[j], lista[j+1] = lista[j+1], lista[j]
print (lista)

