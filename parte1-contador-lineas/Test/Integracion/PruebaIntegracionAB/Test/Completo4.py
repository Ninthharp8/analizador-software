import re
import Completo1 as c1
import Completo2 as c2
import Completo3 as c3
import math

class MiClasePrincipal:
    def __init__(self):
        self.a = 1
        self.b = 1
        self.c = 1

    def mi_funcion(self):
        """
        Esta es mi primera función y no hace nada en particular
        Pero también sirve para que no haga nada en particular

        Entradas: 
        Salidas:
        """
        try:
            milista = [self.a, self.b, self.c]
            mi_otra_lista = [self.a, self.b, self.c]
            
            i = 0
            while i < 5:
                print(f"While loop 1: {i}")
                i += 1

            self.a = 1
            self.b = 2 
            for i in range(15):
                self.a += self.a + self.b
                print(f"For loop 1: {self.a}")

            if self.a > 1:
                print(f"if statement: {self.a}")
            elif self.a < 1:
                print(f"elif statement: {self.b}")
            else:
                print(f"else statement: {self.a + self.b}")

            j = 0
            while j < 3:
                for k in range(2):
                    print(f"Nested loop: j={j}, k={k}")
                j += 1

            for x in range(3):
                for y in range(2):
                    print(f"Double for loop: x={x}, y={y}")

        except Exception as e:
            print('Error:', e)

        return self.a
    

class MiClaseSecundaria:
    """
    Esta es mi segunda clase, está diseñada para
    resolver problemas como:
    if a == b:
        print(a)

    if a != b:
        print(a)

    """

    def primera_funcion(self, a, b):
        for i in range(5):
            if a == b:
                print(f"primera_funcion loop: {i}")
                return a
        pass

    def segunda_funcion(self, a, b):
        i = 0
        while i < 5:
            if a != b:
                print(f"segunda_funcion while loop: {i}")
                return b
            i += 1
        pass

    def tercera_funcion(self, a, b):
        with open("archivo.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)

        for i in range(3):
            if a + b == a:
                print(f"tercera_funcion loop: {i}")
                return a - b
        pass