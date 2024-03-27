import os
import json
import re
import requests
from tabulate import tabulate


def Activos():
    peticion = requests.get('http://154.38.171.54:5502/activos')
    data = peticion.json()
    return data

def CategoriasActivo():
    while True:
        os.system('clear')
        print('''
                                ---CATEGORIAS DE ACTIVOS---

                                    1. Equipo de computo
                                    2. Electrodomestico
                                    3. Juego
                                    0. Regresar al menú de reportes
    ''')
        try:
            opcion = input('\nSeleccione una de las opciones => ')
            if re.match(r'[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 3:
                    if opcion == 1:
                        peticion = requests.get('http://154.38.171.54:5502/activos?idCategoria=1')
                        data = peticion.json()
                        return data
                    elif opcion == 2:
                        peticion = requests.get('http://154.38.171.54:5502/activos?idCategoria=2')
                        data = peticion.json()
                        return data
                    elif opcion == 3:
                        peticion = requests.get('http://154.38.171.54:5502/activos?idCategoria=3')
                        data = peticion.json()
                        return data 
                    elif opcion == 0:
                        break

        except KeyboardInterrupt:
            print('\nRegresando al menú de reportes...')

def ActivosDadosDeBaja():
    peticion = requests.get('http://154.38.171.54:5502/activos?idEstado=2')
    data = peticion.json()
    return data

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
                    6. Regresar al menú  principal
''')
        try:
            opcion = input('\nSeleccione una de las opciones => ')
            if re.match(r'[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 6:
                    if opcion == 1:
                        print(tabulate(Activos(), headers='keys', tablefmt='fancy_grid'))
                        input('Presiona la tecla Enter para continuar...')
                    elif opcion == 2:
                        while True:
                            print(tabulate(CategoriasActivo(), headers='keys', tablefmt='fancy_grid'))
                            print("""
                            
                            
                                        ¿Deseas observar las demas categorias?
                                
                                                        1. Si
                                                        2. No
""")
                            opcion = input('\nSeleccione una de las opciones => ')
                            try:
                                if re.match(r'[0-9]+$', opcion):
                                    opcion = int(opcion)
                                    if opcion >= 1 and opcion <= 2:
                                        if opcion == 1:
                                            print(tabulate(CategoriasActivo(), headers='keys', tablefmt='fancy_grid'))
                                        elif opcion == 2:
                                            break  
                            except KeyboardInterrupt:
                                print()
                    elif opcion == 3:
                        print(tabulate(ActivosDadosDeBaja(), headers='keys', tablefmt='fancy_grid'))
                        input('Presiona la tecla Enter para continuar...')

                        # STANDBY

                    # elif opcion == 4:
                    #     listarActivosAsignacion()
                    # elif opcion == 5:
                    #     listarHistorialMovimientoActivos()
                    # elif opcion == 6:
                        break

        except KeyboardInterrupt:
            print('\nSeleccione una de las opciones => ')
            

