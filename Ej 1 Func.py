def area_rect (b, a):

    area = b*a
    
    return area

base=int(input("ingrese base"))
altura=int(input("ingrese altura"))

resultado = area_rect (base,altura)

print(f'el area del rectangulo es {resultado}')