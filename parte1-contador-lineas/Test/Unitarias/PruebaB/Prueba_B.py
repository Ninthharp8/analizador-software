import Analizador_De_Codigo as LOC

class PruebaDeCodigo:

    def __init__(self):
        """
        Constructor de la clase. Llama a los métodos de prueba relacionados con las estructuras lógicas.
        """
        self.testIf()
        self.testFor()
        self.testWhile()
        self.testDef()
        self.testClass()
        self.testTry()
        self.testWith()
        self.testEstructurasCompletas()

    def testIf(self):
        """
        Este test evalúa una estructura if.

        Salida esperada:
        Líneas lógicas = 3
        """
        print('Test If')
        ruta = 'Test/If.py'
        lineas_logicas_esperadas = 3

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testFor(self):
        """
        Este test evalúa una estructura for.

        Salida esperada:
        Líneas lógicas = 2
        """
        print('Test For')
        ruta = 'Test/For.py'
        lineas_logicas_esperadas = 2

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testWhile(self):
        """
        Este test evalúa una estructura while.

        Salida esperada:
        Líneas lógicas = 2
        """
        print('Test While')
        ruta = 'Test/While.py'
        lineas_logicas_esperadas = 2

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testDef(self):
        """
        Este test evalúa una estructura def.

        Salida esperada:
        Líneas lógicas = 3
        """
        print('Test Def')
        ruta = 'Test/Def.py'
        lineas_logicas_esperadas = 3

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testClass(self):
        """
        Este test evalúa una estructura class.

        Salida esperada:
        Líneas lógicas = 2
        """
        print('Test Class')
        ruta = 'Test/Class.py'
        lineas_logicas_esperadas = 2

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testTry(self):
        """
        Este test evalúa una estructura try.

        Salida esperada:
        Líneas lógicas = 2
        """
        print('Test Try')
        ruta = 'Test/Try.py'
        lineas_logicas_esperadas = 1

        analizador = LOC.AnalizadorDeCodigo(ruta) 
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testWith(self):
        """
        Este test evalúa una estructura with.

        Salida esperada:
        Líneas lógicas = 2
        """
        print('Test With')
        ruta = 'Test/With.py'
        lineas_logicas_esperadas = 2

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testEstructurasCompletas(self):
        """
        Este test evalúa un archivo que contiene if, for, while, def,
        class, try, y with.

        Salida esperada:
        Líneas lógicas = 8 (una por cada estructura detectada).
        """
        print('Test Estructuras Completas')
        ruta = 'Test/EstructurasCompletas.py'
        lineas_logicas_esperadas = 8

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')


# Ejecutar las pruebas
PruebaDeCodigo()