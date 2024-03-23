import re
import json
import os 


# def postPersonal():


# def deletePersonal():


# def editPersonal():


# def searchAsignacionActivos():
        #Para obtener un activo específico por su ID: GET /activos/{id}



def menuPersonal():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ PERSONAL---

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
                        postPersonal()
                    elif opcion == 2:
                        deletePersonal()
                    elif opcion == 3:
                        editPersonal()
                    elif opcion == 4:
                        searchPersonal()
                    elif opcion == 5:
                        break

        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')