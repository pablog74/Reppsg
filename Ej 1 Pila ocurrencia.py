class nodoPila(object) :
    """Clase nodo pila"""
    info, sig = None, None

class Pila(object) :
    """Clase Pila"""
    def __init__(self) :
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato) :
        """Apila el elemento sobre la cima de la pila"""
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima

        self.cima = nodo
        self.tamanio += 1

    def desapilar(self) :
        """Desapila el elemento de la cima de la pila y lo devuelve"""
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1

        return x

    def pila_vacia(self) :
        """Devuelve true si la pila está vacía"""
        return self.cima is None

    def en_cima(self) :
        """Devuelve el valor almacenado en la cima de la pila"""
        if self.cima is not None :
            return self.cima.info
        else :
            return None

    def tamanio(self) :
        """Devuelve el nro de elementos en la pila"""
        return self.tamanio
    
pdatos = Pila()
elementos=[1,2,3,4,5,7,8,6,5,5,4,3,2,2,8,8,8,4,5,7,5,9,6,9,0,9,8]

# Ingresar los elementos en la pila

for num in elementos:
    pdatos.apilar(num)

dato= int(input("Ingrese el número a buscar "))  #Le solicito al usuario en número a buscar

contador = [0,0,0,0,0,0,0,0,0,0]

while (not pdatos.pila_vacia()): #para contabilizar cada ocurrencia
    num=pdatos.desapilar()
    contador[num] += 1

print (f'Se contaron {contador [dato]} veces el número {dato}')



#VER VIDEO CON OTRA OPCION PARA CONTADOR    