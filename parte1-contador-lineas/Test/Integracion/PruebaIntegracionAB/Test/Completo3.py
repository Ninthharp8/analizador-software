import re
import Completo1 as c1
import Completo2 as c2
import Completo3 as c3
import math

class estaEsmiClase:
    def miFuncion():
        """"
        Esta es mi primera funcion y no hace nada en particular
        Pero tambien sirve para que no haga nada en particular

        Entradas: 
        Salidas:
        """
        try:
            a = 1
            b = 1
            c = 1
            milista = [a, b, c]
            miOtraLista = [a, 
                           b, c]
            
            while i < 5:
                print(i)
                i += 1

            a = 1
            b = 2 
            for i in range(15):
                a += a+b

            if a > 1:
                print(a)
            elif a < 1:
                print(b)
            else:
                print(a+b)

        except:
            print('Hola mundo')

        return a
    

    

class estaEsmiClase2:
    """"
    Esta es mi segunda clase, esta diseñada para
    resolver problemas como:
    if a == b:
        print(a)

    if a != b:
        print(a)

    """

    def primeraF(a, b):
        if a == b:
            return a
        pass

    def segundaF(a, b):
        if a != b:
            return b
        pass

    def terceraF(a, b):
        with open("archivo.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)

        if a + b == a:
            return a - b
        pass

    



