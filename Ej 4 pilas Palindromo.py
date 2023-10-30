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
    
ppalabra = Pila()
pila1 = Pila()
pila2 = Pila()

texto = input("Ingrese palabra o texto ")

for x in texto:
    if x != " ":
        ppalabra.apilar(x)
        pila1.apilar(x)

while not pila1.pila_vacia(): 
    x2 = pila1.desapilar()
    pila2.apilar(x2)

while not ppalabra.pila_vacia() and not pila2.pila_vacia() and ppalabra.en_cima() == pila2.en_cima():
    x2 = ppalabra.desapilar()
    x2 = pila2.desapilar()

if ppalabra.pila_vacia():
    print ("Es un palindromo")
else:
    print("No es un palindromo")



