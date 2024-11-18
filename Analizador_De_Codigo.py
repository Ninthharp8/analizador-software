class AnalizadorDeCodigo:
    """
        Analiza el archivo línea por línea para contar las líneas físicas, 
        lógicas y de comentarios.

        Lee el archivo especificado en file_path y realiza el conteo de:
        - Líneas Físicas (aquellas que no son comentarios ni líneas vacías).
        - Líneas de código lógicas.
    """

    def __init__(self, ruta_del_archivo):
        self.ruta_del_archivo = ruta_del_archivo
        self.lineas_fisicas = 0
        self.lineas_logicas = 0

        # Lista de palabras clave que inician bloques lógicos
        self.palabras_clave_logicas = [
            'if', 'elif', 'for', 'while', 'def',
            'class', 'try', 'except', 'with'
        ]

    def analizar_archivo(self):
        comentario_bloque = False

        with open(self.ruta_del_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea_sin_espacios = linea.strip()

                """
                Manejo de comentarios en bloque ignora comentarios en bloque si estos estan en cualquier 
                parte del archivo o si estan en una misma linea.
                """

                if '"""' in linea_sin_espacios or "'''" in linea_sin_espacios:
                    # Si el bloque de comentarios empieza y termina en la misma línea, lo ignoramos.
                    if linea_sin_espacios.count('"""') == 2 or linea_sin_espacios.count("'''") == 2:
                        continue
                    # Si ya estamos dentro de un bloque de comentarios, marcamos que terminó el bloque.
                    if comentario_bloque:
                        comentario_bloque = False
                        continue
                    # Si encontramos el inicio de un bloque de comentarios, marcamos que estamos dentro del bloque.
                    comentario_bloque = True
                    continue

                # decidimos si ignorar o no lo procecesado. si es True se salta la linea y no se cuenta.
                if comentario_bloque:
                    continue

                # Ignorar líneas en blanco
                if not linea_sin_espacios:
                    continue

                # Ignorar líneas que son comentarios
                if linea_sin_espacios.startswith('#'):
                    continue

                # Contar líneas físicas
                self.lineas_fisicas += 1

                # Contar líneas lógicas solo si están definidas en las palabras clave
                primera_palabra = linea_sin_espacios.split()[0]
                if primera_palabra.rstrip(':') in self.palabras_clave_logicas:
                    self.lineas_logicas += 1

    def informe(self):
        """
        Imprime un resumen del análisis realizado sobre el archivo de código.

        Muestra el número de líneas físicas excluyendo comentarios y espacios en blanco.
        El número de líneas de código lógicas.
        """
        print("-" * 60)
        print(f"{'\nPrograma \t\t':<10} | {'LOC Lógicas':<11} \t | {'LOC Físicas':<11}")
        print(f"{self.ruta_del_archivo:<10} \t | {self.lineas_logicas:<11}\t | {self.lineas_fisicas:<11}\n")


if __name__ == "__main__":
    # Para pruebas con un solo archivo. Si son varios, usa AutoTest.py
    ruta_del_archivo = './pruebas/Prueba_A.py'
    analizador = AnalizadorDeCodigo(ruta_del_archivo)
    analizador.analizar_archivo()
    analizador.informe()
