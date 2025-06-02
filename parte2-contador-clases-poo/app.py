"""
Programa: Contador de clases y métodos
Autor: Equipo 6
Fecha: 20 de noviembre del 2024
Descripción:
    Este programa permite al usuario analizar archivos Python POO ubicados en 
    la carpeta analizador para contar lineas de código físicas y logicas, asi 
    como el número de clases y métodos de esta. 
    Utiliza una clase llamada AnalizadorEstructural para realizar el análisis
    detallado de cada archivo Python y proporciona un informe con el conteo de 
    las físicas, logicas, el número de clases y métodos de estas. 
"""

import os
from Analizador_De_Clases_Y_metodos import AnalizadorEstructural

class app:
    """
    Clase principal que gestiona la interacción con el usuario y la ejecución del análisis
    de archivos Python dentro de una carpeta específica.
    """

    def __init__(self, carpeta='./analizador'):
        """
        Inicializa la clase con la ruta de la carpeta donde se buscarán los archivos a analizar.
        Si la carpeta no existe, se crea automáticamente.
        """
        self.carpeta = carpeta
        # Crear la carpeta si no existe
        if not os.path.exists(self.carpeta):
            os.mkdir(self.carpeta)

    def mostrar_bienvenida(self):
        """
        Muestra el mensaje de bienvenida al usuario.
        """
        print("\nBienvenido al Analizador de Clases y Métodos.\n")
        print("Por favor, asegúrate de que los archivos a analizar se encuentren en la carpeta 'analizador'.")
        print("Escribe los nombres de los archivos a analizar, separados por comas.")
        print("Ejemplo: Archivo_ABC.py, Archivo_XYZ.py\n")

    def obtener_archivos(self):
        """
        Solicita al usuario los nombres de los archivos a analizar y los devuelve como una lista.
        """
        entrada = input("Ingresa el nombre de los archivos a analizar: ")
        archivos = [archivo.strip() for archivo in entrada.split(',')]
        return archivos

    def validar_archivo(self, file_path):
        """
        Verifica si el archivo existe y si es un archivo Python (.py).
        """
        return os.path.isfile(file_path) and file_path.endswith('.py')

    def llamar_analizador(self, archivo):
        """
        Realiza el análisis de un archivo Python utilizando la clase `AnalizadorEstructural`.
        """
        file_path = os.path.join(self.carpeta, archivo)
        if self.validar_archivo(file_path):
            try:
                print(f"\nAnalizando archivo: {archivo}")
                print("-" * 60)
                analizador = AnalizadorEstructural(file_path)
                analizador.informe()
            except FileNotFoundError:
                print(f"Error: No se encontró el archivo '{archivo}'.")
            except Exception as e:
                print(f"Error al procesar el archivo '{archivo}': {e}")
        else:
            print(f"Error: El archivo '{archivo}' no es válido o no existe.")

    def ejecutar(self):
        """
        Ejecuta el flujo principal del programa.
        """
        while True:
            self.mostrar_bienvenida()
            archivos = self.obtener_archivos()

            for archivo in archivos:
                self.llamar_analizador(archivo)

            continuar = input("\n¿Deseas analizar más archivos? (si/no): ").strip().lower()
            if continuar != 'si':
                print("\nGracias por usar el Analizador de Código. ¡Hasta luego!")
                break

if __name__ == "__main__":
    analizador = app()
    analizador.ejecutar()
