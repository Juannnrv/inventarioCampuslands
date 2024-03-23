import os
import json
import re















def menuMovimientoActivos():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ MOVIMIENTOS DE ACTIVOS---

                            1. Retorno de activo
                            2. Dar de baja activo
                            3. Cambiar asignación de activo
                            4. Enviar a garantía de activo
                            5. Regresar al menù principal
''')
        try:
            opcion = (input('\n Seleccione una de las opciones => '))
            if(re.match(r'[0-9]+$', opcion) is not None):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 5:
                    if opcion == 1:
                        postActivos()
                    elif opcion == 2:
                        deleteActivos()
                    elif opcion == 3:
                        editActivos()
                    elif opcion == 4:
                        searchActivos()
                    elif opcion == 5:
                        break
                    
        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')