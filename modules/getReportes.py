import os
import json
import re

#def listarActivos():
#http://url/activos

#def listarActivosCategoria():
#http://url/activos?categoria={categoria}

#def listarActivosDebaja():
#http://url/activos?estado=2

#def listarActivosAsignacion():


#def listarHistorialMovimientoActivos():











def menuReportes():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ REPORTES---

                    1. Listar todos los activos
                    2. Listar activos por categoría
                    3. Listar activos por dados de baja por daño
                    4. Listar activos y asignación
                    5. Listar historial de mov. de activo
                    6. Regresar al menú principal
''')
        try:
            opcion = input('\nSeleccione una de las opciones => ')
            if re.match(r'[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 6:
                    if opcion == 1:
                        listarActivos()
                    elif opcion == 2:
                        listarActivosCategoria()
                    elif opcion == 3:
                        listarActivosDeBaja()
                    elif opcion == 4:
                        listarActivosAsignacion()
                    elif opcion == 5:
                        listarHistorialMovimientoActivos()
                    elif opcion == 6:
                        break

        except KeyboardInterrupt:
            print('\nSeleccione una de las opciones => ')

