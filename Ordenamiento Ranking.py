datos = {
    "autos": ["FIAT Cronos", "Peugeot 208", "Toyota Hilux", "Wolk Hilux", "Chevrolet Cruze"], 
    "concesionarias": ["Valmotors FIAT", "Kansai Toyota", "Le meridien Peugeot", "San Jorge", "Dietrich"],
    "registros": [
    {'nro_registro': 1, 'nro_concesionaria': 2, 'nro_producto': 3, 'ventas': 14543},
    {'nro_registro': 2, 'nro_concesionaria': 4, 'nro_producto': 5, 'ventas': 10605},
    {'nro_registro': 3, 'nro_concesionaria': 1, 'nro_producto': 1, 'ventas': 25580},
    {'nro_registro': 4, 'nro_concesionaria': 5, 'nro_producto': 4, 'ventas': 10605},
    {'nro_registro': 5, 'nro_concesionaria': 3, 'nro_producto': 2, 'ventas': 10605},
]
}

def ranking (datos):
    burbuja(datos['registros'])

    imprimir_ranking (datos['registros'], datos['concesionarias']) 

def burbuja (lista):    

    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] ['ventas'] < lista[j+1]['ventas']) :
                lista[j], lista[j+1] = lista[j+1], lista[j]

def imprimir_ranking(registros, concecionarias):
    for registro in registros:
        print(f'{concecionarias[registro["nro_concesionaria"]-1]}:{registro["ventas"]} ventas')

ranking (datos)
