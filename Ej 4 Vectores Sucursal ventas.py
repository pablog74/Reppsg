lista = []
nro_suc = int(input("Nro de sucursal: "))

total_cadena=0


while (nro_suc != 0):
    nombre = input("Nombre de sucursal: ")
    ventas = int(input("Cantidad de ventas: "))
    total = int(input("Venta total de la sucursal: "))
    total_cadena += total

    lista.append([nro_suc, nombre, ventas, total, total/ventas, total_cadena])

    nro_suc = int(input("Nro de sucursal: "))

for suc in lista:
    print (f"Nro Sucursal: {suc[0]}")
    print (f"Sucursal: {suc[1]}")
    print (f"Ventas: {suc[2]}")
    print (f"Total Sucursal: {suc[3]}")
    print (f"Promedio: {suc[4]}")
    print (f"Total venta de la cadena: {suc[5]}")
    


