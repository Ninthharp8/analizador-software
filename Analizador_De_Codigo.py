"""
Analizador de líneas de código en Python.

Esta Modulo analiza un archivo fuente en Python y cuenta:
- Líneas físicas: excluye comentarios y líneas en blanco.
- Líneas lógicas: bloques lógicos como clases, funciones, etc.
"""

class AnalizadorDeCodigo:

    """
    Clase para analizar archivos Python y contar líneas físicas y lógicas.

    Attributes:
        ruta_del_archivo (str): Ruta del archivo a analizar.
        lineas_fisicas (int): Contador de líneas físicas.
        lineas_logicas (int): Contador de líneas lógicas.
    """

    def __init__(self, ruta_del_archivo):
        """
        Inicializa el analizador con la ruta del archivo.

        Args:
            ruta_del_archivo (str): Ruta del archivo a analizar.
        """
        self.ruta_del_archivo = ruta_del_archivo
        self.lineas_fisicas = 0
        self.lineas_logicas = 0
        self.palabras_clave_logicas = ['if','for','while','def','class','try','with']

    def analizar_archivo(self):

        """
        Analiza un archivo fuente para contar líneas físicas y lógicas.

        Procesa línea por línea el archivo especificado, ignorando comentarios
        y líneas en blanco. Los comentarios en bloque también se excluyen.

        Returns:
            nada
        Excepciones:
            FileNotFoundError: Si el archivo no existe.
            IOError: Si hay un problema al leer el archivo.
        """
        comentario_bloque = False
        try:
            with open(self.ruta_del_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    linea_sin_espacios = linea.strip()

                    # Manejo de comentarios en bloque
                    if '"""' in linea_sin_espacios or "'''" in linea_sin_espacios:
                        if linea_sin_espacios.count('"""') == 2 or linea_sin_espacios.count("'''") == 2:
                            continue
                        comentario_bloque = not comentario_bloque
                        continue
                    # Manejo de lineas en blanco y comentarios normales
                    if comentario_bloque or not linea_sin_espacios or linea_sin_espacios.startswith('#'):
                        continue

                    self.lineas_fisicas += 1

                    primera_palabra = linea_sin_espacios.split()[0]
                    if primera_palabra.rstrip(':') in self.palabras_clave_logicas:
                        self.lineas_logicas += 1

        except FileNotFoundError:
            print(f"Error: El archivo {self.ruta_del_archivo} no existe.")
        except IOError as e:
            print(f"Error al leer el archivo {self.ruta_del_archivo}: {e}")
        except UnicodeDecodeError:
            print(f"Error: El archivo {self.ruta_del_archivo} no es un \
                  archivo de texto válido.")

    def informe(self):

        """
        Retorna un resumen tabular del análisis del archivo.

        Retorna:
            El conteo de las lineas de codigo físicas y lógicas.
        """
        print("-" * 60)
        print(f"{'Programa':<30} | {'LOC Lógicas':<11} | {'LOC Físicas':<11}")
        print(f"{self.ruta_del_archivo:<30} | {self.lineas_logicas:<11} | {self.lineas_fisicas:<11}")


if __name__ == "__main__":
    ruta_del_archivo = './pruebas/Prueba_M.py'
    analizador = AnalizadorDeCodigo(ruta_del_archivo)
    analizador.analizar_archivo()
    analizador.informe()

