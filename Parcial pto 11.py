datos = {
        "celulares": ["Samsung S23", "Motorola Razr 40", "Samsung Z Flip", "Motorola Edge 40", "Xiaomi Redmi Note 11"],
        "sucursal": ["Almagro", "Belgrano", "Caballito", "Devoto", "Flores"],
        "registros": [
            {'nro_registro': 1, 'nro_sucursal': 2, 'nro_producto': 3, 'monto_vendido': 28475},
            {'nro_registro': 2, 'nro_sucursal': 4, 'nro_producto': 5, 'monto_vendido': 43316},
            {'nro_registro': 3, 'nro_sucursal': 1, 'nro_producto': 1, 'monto_vendido': 28960},
            {'nro_registro': 4, 'nro_sucursal': 5, 'nro_producto': 4, 'monto_vendido': 44109},
            {'nro_registro': 5, 'nro_sucursal': 3, 'nro_producto': 2, 'monto_vendido': 32738}
]
}

def rankingSucursales (datos): #funcionpara realizar busqueda en registros donde se encuentran los datos solicitados
    burbuja(datos['registros'])

    imprimir_ranking (datos['registros'], datos['sucursal']) 

def burbuja (lista):    #funcion para comparar monto vendido y ordene x metodo burbuja

    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] ['monto_vendido'] < lista[j+1]['monto_vendido']) :
                lista[j], lista[j+1] = lista[j+1], lista[j]

def imprimir_ranking(registros, sucursal): #defino que datos imprimir
    for registro in registros:
        print(f'{sucursal[registro["nro_sucursal"]-1]}:{registro["monto_vendido"]} monto_vendido')

rankingSucursales (datos)
