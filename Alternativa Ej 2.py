print ("ingrese el primer número")
n1=int(input())

print ("ingrese el segundo número")
n2=int(input())

print ("elija una opción")
print ("1 sumar 2 restar 3 multiplicar")

opcion=(input())

while (opcion > 3 or opcion < 1):
    opcion=(input("elija una opción"))

if (opcion == 1):
    resultado=(n1+n2)

elif (opcion == 2):
    resultado=(n1-n2)

#else resultado = (n1*n2) 


