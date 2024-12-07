import Analizador_De_Codigo as LOC

class PruebaDeCodigo:

    def __init__(self):
        self.testCompleto1()
        self.testCompleto2()
        self.testCompleto3()
        self.testCompleto4()

        pass

    def testCompleto1(self):
        """
        Como primera prueba se utilizara el codigo completo de 
        la primera prueba unitaria de la carpeta 'Prueba_A'

        En ese codigo se esperaba unicamente que se tuviera procesamiento 
        del las lineas fisicas. Ahora se tomara en cuenta tambien las logicas
        que fueron utilizadas.

        Salida esperada:
        Líneas lógicas = 
        Lineas fisicas = 
        """

        print('Test Completo 1')
        ruta = 'Test/Completo1.py'

        lineas_fisicas_esperadas = 30
        lineas_logicas_esperadas = 4

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Fisicas: Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')
        print(f'Logicas: Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas and lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

        return
    
    def testCompleto2(self):
        """ 
        Para esta test se esta utilizando la prueba completa
        de las pruebas unitarias del archivo 'Prueba_B'.
        En esa prueba unicamente se esta tomando en consideracion 
        que el codigo deberia de contar las lineas logicas. 

        Ahora, se procesara para que tome en cuenta ambas lineas, fisicas 
        y logicas. 
        

        Salida esperada:
        Lineas fisicas = 20
        Líneas lógicas = 8 
        """

        print('Test Completo 2')
        ruta = 'Test/Completo2.py'
        lineas_fisicas_esperadas = 20
        lineas_logicas_esperadas = 8

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Fisicas: Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')
        print(f'Logicas: Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas and lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        return
    
    def testCompleto3(self):
        """
        Para este test se esta utilizando una combinacion 
        de todo el estandar de conteo, tanto fisico como logico.
        

        Salida esperada:
        Líneas lógicas = 46
        Lineas fisicas = 14
        """

        print('Test Completo 3')
        ruta = 'Test/Completo3.py'
        lineas_fisicas_esperadas = 46
        lineas_logicas_esperadas = 14

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo() 

        print(f'Fisicas: Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')
        print(f'Logicas: Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas and lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        return
    
    def testCompleto4(self):
        """
        Para este test se esta utilizando una combinacion 
        de todo el estandar de conteo, tanto fisico como logico.
        

        Salida esperada:
        Líneas lógicas = 
        Lineas fisicas = 
        """

        print('Test Completo 4')
        ruta = 'Test/Completo4.py'
        lineas_fisicas_esperadas = 64
        lineas_logicas_esperadas = 22

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Fisicas: Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')
        print(f'Logicas: Resultado esperado {lineas_logicas_esperadas}, resultado obtenido {analizador.lineas_logicas}')

        if lineas_logicas_esperadas == analizador.lineas_logicas and lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        return
    

PruebaDeCodigo()