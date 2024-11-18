"""
    Programa: Analizador de líneas de código
    Autor: Angel Mariel Osalde Salazar
    Fecha: 20 de septiembre del 2024
    Descripción: Este programa analiza un archivo de código fuente de tipo python 
    y cuenta el número total de líneas físicas, líneas de código lógicas y líneas de comentarios, 
    con el fin de proporcionar una estimación de las líneas de código físicas y lógicas.
"""

class CodeAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.total_lines = 0
        self.logical_lines = 0
        self.comment_lines = 0
        self.in_multiline_comment = False

    def analyze_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                self.total_lines += 1
                stripped_line = line.strip()

                # Comentarios multilínea en una sola línea
                if (stripped_line.startswith("'''") and stripped_line.endswith("'''") and len(stripped_line) > 6) or \
                   (stripped_line.startswith('"""') and stripped_line.endswith('"""') and len(stripped_line) > 6):
                    self.comment_lines += 1
                    continue

                # Contar bloques de comentarios multilínea (cada bloque cuenta por 1)
                if self.in_multiline_comment:
                    if stripped_line.endswith("'''") or stripped_line.endswith('"""'):
                        self.in_multiline_comment = False
                    continue

                # Detectar inicio de bloques de comentarios multilínea
                if stripped_line.startswith("'''") or stripped_line.startswith('"""'):
                    self.in_multiline_comment = True
                    self.comment_lines += 1
                    continue

                # Contar comentarios en línea y líneas vacías
                if stripped_line.startswith('#') or not stripped_line:
                    if stripped_line.startswith('#'):
                        self.comment_lines += 1
                else:
                    # Contar líneas de código lógicas
                    if '#' in stripped_line:
                        stripped_line = stripped_line.split('#')[0].strip()
                    if stripped_line:
                        self.logical_lines += 1

    def get_results(self):
        return {
            "Programa": self.file_path.split('/')[-1].split('.')[0],
            "LOC Lógicas": self.logical_lines,
            "LOC Físicas": self.total_lines
        }

def imprimir_tabla(resultados):
    # Encabezado de la tabla
    print(f"{'Programa':<10} | {'LOC Lógicas':<11} | {'LOC Físicas':<11}")
    print("-" * 35)

    # Filas de la tabla
    for resultado in resultados:
        print(f"{resultado['Programa']:<10} | {resultado['LOC Lógicas']:<11} | {resultado['LOC Físicas']:<11}")

if __name__ == "__main__":
    archivos = [
        'C:/Users/Juan Falcon/Videos/pruebas/archivo_ABC.py',  # Cambia esta ruta por la de tu archivo
        'C:/Users/Juan Falcon/Videos/pruebas/archivo_XYZ.py'   # Cambia esta ruta por la de tu archivo
    ]

    resultados = []
    for archivo in archivos:
        analyzer = CodeAnalyzer(archivo)
        analyzer.analyze_file()
        resultados.append(analyzer.get_results())

    # Imprimir resultados en formato de tabla
    imprimir_tabla(resultados)
