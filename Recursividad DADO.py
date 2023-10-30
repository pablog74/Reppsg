from random import*

def adivina_d (x,n):
    nro=int(input("Ingrese número "))
    n += 1

    if (nro==x):
        print (f"acertó en {n} intentos")

    else: 
        adivina_d (x,n)

nro = randint (1,6)
adivina_d (nro, 0) 