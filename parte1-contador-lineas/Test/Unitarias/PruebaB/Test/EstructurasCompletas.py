# Código para evaluar estructuras completas

# Estructura `if`
x = 10
if x > 5:
    print("x es mayor que 5")

# Estructura `for`
numeros = [1, 2, 3]
for n in numeros:
    print(n)

# Estructura `while`
contador = 0
while contador < 5:
    contador += 1

# Estructura `def`
def suma(a, b):
    return a + b

# Estructura `class`
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

# Estructura `try`
try:
    resultado = 10 / 0 
except ZeroDivisionError:
    print("Error: División por cero")

# Estructura `with`
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
