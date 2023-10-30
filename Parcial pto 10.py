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

def maxMinVendido(datos): #defino la funcion y establezco en 0 el maximo y el minimo para luego comparar
    minimo=datos ['registros'][0]
    maximo=datos ['registros'][0]

    for registro in datos ['registros']: # bucle para empezar a comparar
        if registro ['monto_vendido'] < minimo ['monto_vendido']:
            minimo=registro
        
        if registro ['monto_vendido'] > maximo ['monto_vendido']:
            maximo=registro

    imprimirdatos(minimo, maximo, datos['celulares'], datos ['sucursal']) #defino que se va a imprimir

def imprimirdatos (minimo, maximo, celulares, sucursal): #funcion para imprimir datos solicitados

    print (f'Mínimo: {minimo ["monto_vendido"]} ventas de {celulares[minimo["nro_producto"]-1]} en {sucursal[minimo["nro_sucursal"]-1]}')
    print (f'Máximo: {maximo ["monto_vendido"]} ventas de {celulares[maximo["nro_producto"]-1]} en {sucursal[maximo["nro_sucursal"]-1]}')

maxMinVendido(datos)