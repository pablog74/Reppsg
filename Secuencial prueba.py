datos = {
        "celulares": ["Samsung S23", "Motorola Razr 40", "Samsung Z Flip", "Motorola Edge 40", "Xiaomi Redmi Note 11"],
        "sucursal": ["Almagro", "Belgrano", "Caballito", "Devoto", "Flores"],
        "registros": [
            {'nro_registro': 1, 'nro_sucursal': 2, 'nro_producto': 3, 'monto_vendido': 28475},
            {'nro_registro': 2, 'nro_sucursal': 4, 'nro_producto': 5, 'monto_vendido': 43316},
            {'nro_registro': 3, 'nro_sucursal': 1, 'nro_producto': 1, 'monto_vendido': 28960},
            {'nro_registro': 4, 'nro_sucursal': 5, 'nro_producto': 4, 'monto_vendido': 44109},
            {'nro_registro': 5, 'nro_sucursal': 3, 'nro_producto': 2, 'monto_vendido': 32738}]
}

def secuencial(lista, sucursal) :
 """ Metodo de busqueda secuencial """
 posicion = -1
 for i in range(0, len(lista)) :
    if (lista[i] == sucursal) :
        posicion = i
 return posicion

print ("flores")
