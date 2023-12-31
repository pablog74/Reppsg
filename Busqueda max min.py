datos = {
    "autos": ["FIAT Cronos", "Peugeot 208", "Toyota Hilux", "Wolk Hilux", "Chevrolet Cruze"], 
    "concesionarias": ["Valmotors FIAT", "Kansai Toyota", "Le meridien Peugeot", "San Jorge", "Dietrich"],
    "registros": [
    {'nro_registro': 1, 'nro_concesionaria': 2, 'nro_producto': 3, 'ventas': 14543},
    {'nro_registro': 2, 'nro_concesionaria': 4, 'nro_producto': 5, 'ventas': 10605},
    {'nro_registro': 3, 'nro_concesionaria': 1, 'nro_producto': 1, 'ventas': 25580},
    {'nro_registro': 4, 'nro_concesionaria': 5, 'nro_producto': 4, 'ventas': 12525},
    {'nro_registro': 5, 'nro_concesionaria': 3, 'nro_producto': 2, 'ventas': 15282},
]
}

def maxminventas (datos):
    minimo=datos ['registros'][0]
    maximo=datos ['registros'][0]

    for registro in datos ['registros']:
        if registro ['ventas'] < minimo ['ventas']:
            minimo=registro
        
        if registro ['ventas'] > maximo ['ventas']:
            maximo=registro

    imprimirdatos(minimo, maximo, datos['autos'], datos ['concesionarias'])

def imprimirdatos (minimo, maximo, autos, concesionarias):

    print (f'Mínimo: {minimo ["ventas"]} ventas de {autos[minimo["nro_producto"]-1]} en {concesionarias[minimo["nro_concesionaria"]-1]}')
    print (f'Máximo: {maximo ["ventas"]} ventas de {autos[maximo["nro_producto"]-1]} en {concesionarias[maximo["nro_concesionaria"]-1]}')

maxminventas (datos)


