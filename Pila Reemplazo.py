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

Pila1 = [1,1,2,3,4,5,6,7,8,9,10]
Pila2 = []

dato1 = int(input("ingresa R"))
dato2 = int(input("ingresa N "))

while Pila1:
    dato = Pila1.pop()
    if (dato != dato1):
        Pila2.append (dato)
    else:
        Pila1.append(dato2)    
        break
while Pila2:
    Pila1.append (Pila2.pop())

print ("Dato reemplazado")
print (Pila1)

