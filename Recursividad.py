def regresiva (nro):
 
   if (nro == 0):
        print ("Booom")
        return
   else:
       print (nro)
       nro=nro-1
       
       regresiva (nro) 
       return
   
nro=int(input("Ingrese un número "))
regresiva (nro)

