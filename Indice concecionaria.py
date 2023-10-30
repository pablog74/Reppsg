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

def buscarconcesionaria (datos, concesionaria):
    
    posicionA=binaria(datos['concesionarias'], concesionaria)

    posicionB=secuencial(datos['registros'],posicionA + 1)

    imprimirDatos (datos):

def secuencial(lista, buscado) :
 
    posicion = -1
    for i in range(0, len(lista)) :
        if (lista[i] ['nro_concesionaria'] == buscado) :
            posicion = i
    return posicion


def binaria(lista, buscado) :
 
    posicion = -1
    primero = 0
    ultimo = len(lista) - 1
 
    while (primero <= ultimo) and (posicion == -1) :
        medio = (primero + ultimo) // 2
 
        if (lista[medio] == buscado) :
            posicion = medio
        else :
            if (buscado < lista[medio]) :
                ultimo = medio - 1
            else :
                primero = medio + 1
    return posicion


buscarconcesionaria (datos, 'Dietrich')