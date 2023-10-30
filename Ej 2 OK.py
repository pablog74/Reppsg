print ("ingrese el primer número")
n1=int(input())

print ("ingrese el segundo número")
n2=int(input())

print ("elija una opción")

print ("1 sumar 2 restar 3 multiplicar")


def suma (n1, n2):
    return n1+n2
def resta (n1, n2):
    return n1-n2
def multiplica (n1, n2):
    return n1*n2

opcion=(input())



if opcion == '1':
    print (f"el resultado es, {suma(n1,n2)}" )

elif opcion == '2':
    print (f"el resultado es, {resta(n1,n2)}" )

elif opcion == '3':
    print (f"el resultado es, {multiplica(n1,n2)}" )




