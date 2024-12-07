import Analizador_De_Codigo as LOC

class PruebaDeCodigo:
    
    def __init__(self):
        """
    
        """
        self.testComentarios()
        self.testDeclaraciones()
        self.testImportaciones()
        self.testLogicas()
        self.testCompleto()

    def testComentarios(self):
        """
        Este test contiene unicamente comentarios (una sola linea y mutiples)
        y lineas vacias, se espera que el analizador no detecte ninguna de estas lineas.
        
        El codigo tiene dentro la simulacion de codigo pero se encuentra dentro de 
        un comentario. Por lo que no se deberia de considerar como parte de una linea
        fisica.
        
        Salida esperada para considerarlo como prueba aprobada

        Lineas fisicas = 0 
        """
        print('Test de Comentarios')
        ruta = '/Test/Comentarios.py'
        lineas_fisicas_esperadas = 0
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo
        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        return 
    
    def testDeclaraciones(self):
        """
        Este test contiene declaraciones de una sola linea y multiples. 

        Salida esperada para considerarlo como test aprobado
        Lineas fisicas = 14
        """
        print('Test de Declaraciones')
        ruta = 'Test/Declaraciones.py'
        lineas_fisicas_esperadas = 14

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo() 

        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        return 
    
    def testImportaciones(self):
        """
        Este test contiene unicamente importaciones de librerias.

        Salida esperada para considerarlo como test aprobado
        Lineas fisicas = 4

        """
        print('Test de Importaciones')
        ruta = 'Test/Imports.py'
        lineas_fisicas_esperadas = 4

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo() 
        
        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        return 
    
    
    def testLogicas(self):
        """
        Este test contiene una conjunto de operaciones logicas
        y declaraciones.

        Salida esperada para considerarlo como test aprobado
        Lineas fisicas = 12

        """
        print('Test de Logicas')
        ruta = 'Test/Logicas.py'
        lineas_fisicas_esperadas = 12

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()  
        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        return 


    def testCompleto(self):
        """
        Este test contiene el contenido de todos los test anteriores,
        tomando en cuenta eso, la salida deberia ser la suma de todos los test.

        Salida esperada para considerarlo como test aprobado
        Lineas fisicas = 30

        """
        print('Test de Completo')
        ruta = 'Test/Completo.py'
        lineas_fisicas_esperadas = 30

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()  
        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        return 
    
PruebaDeCodigo()
