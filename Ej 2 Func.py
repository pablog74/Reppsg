def area_circulo (pi, r):

    area=pi * r ** 2

    return area

pi=3.14
ra=float(input("ingrese el radio"))

resultado=area_circulo (pi, ra)

print(f'el area del circulo es {resultado}')