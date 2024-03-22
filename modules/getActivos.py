import os
import json
import re


# URL DATA


            









def menuActivos():
    while True:
        os.system('clear')
        print('''
                               ---MENÙ ACTIVOS---

                            1. Agregar
                            2. Editar
                            3. Eliminar
                            4. Buscar
                            5. Regresar al menù principal
''')
        opcion = (input('\n Seleccione una de las opciones => '))
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if (opcion>=0 and opcion<=5):
                if opcion == 1:
                    postActivos()
                if opcion == 2:
                    deleteActivos()
                if opcion == 3:
                    updateActivos()

                    
