import os
import json
import re
import requests
from tabulate import tabulate
import modules.getActivos as gA


def postAsignacionActivos():
    
    data = gA.Activos()
        
    
    while True:
        # os.system('clear')
        print("""
        A continuación agregaras una nueva asignación a un activo existente en SISTEMA G&C DE INVENTARIO CAMPUSLANDS
        
                                                ¿Deseas continuar?
                            
                                                    1. Si
                                                    2. No
""")
        opcion = input('\nSeleccione una de las opciones => ')
        try:
            if re.match(r'[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion >= 1 and opcion <= 2:
                    if opcion == 1:
                        idPost = input('\nIngrese el ID del activo en el cual deseas crear una asignación en SISTEMA G&C DE INVENTARIO CAMPUSLANDS => ')
                        # Validar ID del activo
                        if not any(activo["id"] == idPost for activo in data):
                            raise Exception('\n---> El ID del activo no existe')

                        NroAsignacion = input('\nIngrese el número de asignación del activo => ')
                        # Validar número de asignación
                        if not re.match(r'[0-9]+$', NroAsignacion):
                            raise Exception('\n---> El número de asignación no es válido')

                        FechaAsignacion = input('\nIngrese la fecha de asignación (YYYY-MM-DD) => ')
                        # Validar fecha de asignación
                        if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', FechaAsignacion):
                            raise Exception('\n---> La fecha de asignación no tiene el formato correcto')
                        
                        print("""
                            ¿Se le asignó el activo a una Zona o Persona?
                            
                                            1. Zona
                                            2. Persona
                            """)
                        TipoAsignacion = input('\nSeleccione una de las opciones => ')
                        if re.match(r'^[0-9]+$', TipoAsignacion):
                            if opcion == 1:
                                TipoAsignacion = 'Zona'
                            if opcion == 2:
                                TipoAsignacion = 'Personal'
                        else:
                            raise Exception('\n---> Tipo de asignación no válido')
                        
                        AsignadoA = input('\nIngresa el ID de la persona o zona a la cual le fue asignado el activo => ')
                        if not re.match(r'^[0-9]+$', AsignadoA):
                            raise Exception('\n---> ID de asignación no válido')

                        # Agregar la nueva asignación al activo correspondiente
                        for activo in data:
                            if activo["id"] == idPost:
                                # Comprobamos si ya existe una asignación con el mismo número
                                for asignacion in activo["asignaciones"]:
                                    if "NroAsignacion" in asignacion and asignacion["NroAsignacion"] == NroAsignacion:
                                        raise Exception('\n---> El número de asignación ya existe para este activo')
                                # Si no se encontró una asignación con el mismo número, agregamos la nueva asignación al mismo diccionario
                                activo["asignaciones"].append({"NroAsignacion": NroAsignacion, "FechaAsignacion": FechaAsignacion, "TipoAsignacion": TipoAsignacion, "AsignadoA": AsignadoA})
                                break

                        print('\nAsignación creada satisfactoriamente.')
                            
                        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
                        peticion = requests.post(f'http://154.38.171.54:5502/activos?id={id}', headers=headers, data=json.dumps(activo, indent=4))
                        res = peticion.json()
                        res['Mensaje'] = '\nAsignación creada satisfactoriamente'
                        print(res['Mensaje'])  
                        input('\nPresione Enter para continuar...')
                        return [res]
                        
                    elif opcion == 2:
                        break
                        
            else:
                raise Exception ('---> El dato ingresado debe ser 1 o 2')
                        
        except Exception as error:
            print('\n---ERROR---')
            print(error)
            break


# def searchAsignacionActivos():
        #Para obtener un activo específico por su ID: GET /activos/{id}



def menuAsignacionActivos():
    while True:
        # os.system('clear')
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
                    # elif opcion == 2:
                    #     searchAsignacionActivos()
                    elif opcion == 3:
                        break
        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')