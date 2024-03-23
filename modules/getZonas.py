import re
import json
import os 


# def postZonas():


# def deleteZonas():


# def editZonas():


# def searchAsignacionActivos():
        #Para obtener un activo específico por su ID: GET /activos/{id}



def menuZonas():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ ZONAS---

                        1. Agregar
                        2. Editar
                        3. Eliminar
                        4. Buscar
                        5. Regresar al menú principal
''')
        try:
            opcion = (input('\n Seleccione una de las opciones => '))
            if(re.match(r'[0-9]+$', opcion) is not None):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 5:
                    if opcion == 1:
                        postZonas()
                    if opcion == 2:
                        deleteZonas()
                    if opcion == 3:
                        editZonas()
                    if opcion == 4:
                        searchZonas()
                    if opcion == 5:
                        break

        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')