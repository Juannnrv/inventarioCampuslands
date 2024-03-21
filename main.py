import os
import re


if __name__ == "__main__":
    while True:
        os.system('clear')
        print('''
                    ---SISTEMA G&C DE INVENTARIO CAMPUSLANDS---

                            1. Activos
                            2. Personal
                            3. Zonas
                            4. Asignación de activos
                            5. Reportes
                            6. Movimiento de activos
                            7. Salir
''')
        opcion = int(input('\nSeleccione una de las opciones => '))
        if re.match(r'[0-9]+$', opcion):
            opcion = int(opcion)
            if opcion >= 0 and opcion <= 7:

                # AQUI IRAN LOS MENÚS DE ACUERDO A SU OPCIÓN

                break
                
                
    
    