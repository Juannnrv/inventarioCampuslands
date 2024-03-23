import os
import json
import re


# URL DATA

# def postActivos():

# def deleteActivos():

# def editActivos():

# def searchAsignacionActivos():
        #Para obtener un activo específico por su ID: GET /activos/{id}









def menuActivos():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ ACTIVOS---

                        1. Agregar
                        2. Editar
                        3. Eliminar
                        4. Buscar
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
                    

                    
