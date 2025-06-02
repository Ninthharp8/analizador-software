"""
Programa: Sistema Comparador de Versiones
Autor: Equipo 6
Fecha: 26 de noviembre de 2024

Descripción:
    Esta aplicación permite comparar dos versiones de archivos Python, analizando
    su estructura para obtener  información  sobre  las  clases,  métodos, líneas 
    dentro de las clases, y  el  total  de líneas de código físicas y lógicas. El
    programa genera un informe detallado  con los resultados de las comparaciones 
    y análisis de ambos archivos remarcando las lineas añadidas, eliminadas, 
    movidas y con cambios en 2 archivos nuevos formateados a 80 caracteres por linea.
    
    Funcionalidades:
    - Solicita al usuario los nombres de dos archivos Python para ser comparados.
    - Verifica la validez de los archivos (existencia y extensión `.py`).
    - Analiza la estructura de las clases y métodos de los archivos usando la 
      clase `AnalizadorEstructural`.
    - Compara las diferencias entre las versiones de los archivos a través de la 
      clase `ComparadorArchivos`.
    - Genera informes detallados con los resultados de los análisis y la 
      comparación de los archivos.
    
    Requisitos:
    - Los archivos a analizar deben estar ubicados en la carpeta 'analizador'.
    - Se deben proporcionar exactamente dos archivos para continuar con el 
      análisis.

"""

import os
import time
from Analizador_De_Clases_Y_metodos import AnalizadorEstructural
from Comparador_De_Versiones import ComparadorArchivos  

class App:
    """
    Clase principal que gestiona la interacción con el usuario y la ejecución del análisis
    y comparación de archivos Python dentro de una carpeta específica.
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
        entrada = input("Ingresa el nombre de los dos archivos a analizar: ")
        archivos = [archivo.strip() for archivo in entrada.split(',')]
        return archivos if len(archivos) == 2 else None

    def validar_archivo(self, file_path):
        """
        Verifica si el archivo existe y si es un archivo Python (.py).
        """
        return os.path.isfile(file_path) and file_path.endswith('.py')

    def analizar_archivos(self, archivo1, archivo2):
        """
        Analiza los archivos con la clase `AnalizadorEstructural`.
        Si ambos archivos son válidos, procede a compararlos.
        """
        file_path1 = os.path.join(self.carpeta, archivo1)
        file_path2 = os.path.join(self.carpeta, archivo2)

        if self.validar_archivo(file_path1) and self.validar_archivo(file_path2):
            try:
                print(f"\nAnalizando archivo: {archivo1}")
                analizador1 = AnalizadorEstructural(file_path1)
                analizador1.obtener_resultados()

                print(f"\nAnalizando archivo: {archivo2}")
                analizador2 = AnalizadorEstructural(file_path2)
                analizador2.obtener_resultados()

                # Si ambos análisis son exitosos, proceder a la comparación
                comparador = ComparadorArchivos(file_path1, file_path2)
                print("\nComparando archivos...")
                comparador.comparar_archivos()  # Método para comparar y formatear

                # Mostrar informe final de ambos archivos
                print(f"\nInforme del archivo :{archivo1}")
                analizador1.informe()

                print(f"\nInforme del archivo :{archivo2}")
                analizador2.informe()

            except Exception as e:
                print(f"\nError durante el análisis: {e}")
        else:
            print("Error: Uno o ambos archivos no son válidos o no existen.")

    def ejecutar(self):
        """
        Ejecuta el flujo principal del programa.
        """
        while True:
            self.mostrar_bienvenida()
            archivos = self.obtener_archivos()

            if archivos and len(archivos) == 2:
                self.analizar_archivos(archivos[0], archivos[1])
            else:
                print("\nDebes ingresar exactamente dos archivos para continuar.")

            continuar = input("\n¿Deseas analizar más archivos? (si/no): ").strip().lower()
            if continuar != 'si':
                print("\nGracias por usar el Analizador de Código. ¡Hasta luego!")
                time.sleep(5)
                break


if __name__ == "__main__":
    app = App()
    app.ejecutar()
