import os
import json
import re


# def postAsignacionActivos():


# def searchAsignacionActivos():
        #Para obtener un activo específico por su ID: GET /activos/{id}



def menuAsignacionActivos():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ ASIGNACIÓN ACTIVOS---

                            1. Crear asignación
                            2. Buscar asignación
                            3. Regresar al menú principal
                        
''')
        try:
            opcion = input('\nSeleccione una de las opciones => ')
            if re.match(r'^[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 5:
                    if opcion == 1:
                        postAsignacionActivos()
                    elif opcion == 2:
                        searchAsignacionActivos()
                    elif opcion == 3:
                        break
        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')