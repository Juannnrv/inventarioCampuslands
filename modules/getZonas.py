import re
import json
import os 
import requests

def Zonas():
    peticion = requests.get('http://154.38.171.54:5502/zonas')
    data = peticion.json()
    return data

def ZonasID(id):
    for val in Zonas():
        if val.get('id') == id:
            return [val]

def postZonas():
    Zonas = {}
    while True:
        while True:
            os.system('clear')
            print("""
            A continuación agregaras una nueva zona en Campuslands
            
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
                            # while True:
                            #     os.system('clear')
                            #     try:
                            #         if not Zonas.get('id'):
                            #             while True:
                            #                 iD = input('Ingrese el ID de la zona en Campuslands => ')
                            #                 if iD.isdigit():
                            #                     iD = int(iD)
                            #                     data = ZonasID(iD)
                            #                     if data:
                            #                         raise Exception('El ID de la zona en Campuslands ya existe')
                            #                     else:
                            #                         Zonas['id'] = iD
                            #                         break
                            #                 else:
                            #                     raise Exception('---> El ID de la zona en Campuslands no cumple con el formato establecido')
                            #             break

                                    if not Zonas.get('nombreZona'):
                                        nombreZona = input('\nIngrese el nombre de la zona en Campuslands => ')
                                        if re.match(r'^[A-Z]{1}[a-z]+$', nombreZona):
                                            Zonas['nombreZona'] = nombreZona

                                        totalCapacidad = input('Ingrese la capacidad máxima de la zona en Campuslands => ')
                                        if totalCapacidad.isdigit():
                                            totalCapacidad = int(totalCapacidad)
                                            Zonas['totalCapacidad'] = totalCapacidad
                                            
                                            headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
                                            peticion = requests.post('http://154.38.171.54:5502/zonas', headers=headers, data=json.dumps(Zonas, indent=4))
                                            res = peticion.json()
                                            res['Mensaje'] = '\nZona guardada satisfactoriamente'
                                            print(res['Mensaje'])  
                                            input('\nPresione Enter para continuar...')
                                            return [res]

                                        else:
                                            raise Exception('---> El dato ingresado de la zona en Campuslands no cumple con el formato establecido')
                                        
                                    else:
                                        raise Exception('---> El dato ingresado de la zona en Campuslands ya existe')

                                # except Exception as error:
                                #     print('---ERROR---')
                                #     print(error)
                                #     break
                        
                        if opcion == 2:
                            break
                            
            except Exception as error:
                print('---ERROR---')
                print(error)
                break

def deleteZonas(id):
    while True:
        while True:
            os.system('clear')
            print("""
            A continuación eliminaras una zona existente en Campuslands
            
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
                            peticion = requests.delete(f'http://154.38.171.54:5502/zonas/{id}')
                            res = peticion.json()
                            res['Mensaje'] = 'Zona eliminada satisfactoriamente'
                            print()
                            print(res['Mensaje'])
                            input('\nPresione la tecla Enter para poder continuar...')
                            return [res]
                        elif opcion == 2:
                            break
                    else:
                        raise Exception ('---> El dato ingresado debe ser 1 o 2 ')
                else:
                    raise Exception ('---> El dato ingresado debe ser 1 o 2 ')        
            except Exception as error:
                print('---ERROR---')
                print(error)
                break

def editZonas(id):
    data = ZonasID(id)
    if len(data):
        while True:
            os.system('clear')
            print("""
            A continuación editaras un dato de una zona existente en Campuslands
            
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
                            print("""
                    ¿Qué dato deseas actualizar?

                1. Nombre de la zona
                2. Capacidad maxima de la zona
                                    """)
                            opcion = int(input('\nSeleccione una de las opciones => '))
                            if opcion == 1:
                                nombre = input('Ingrese el nuevo nombre de la zona en Campuslands => ')
                                if re.match(r'^[A-Z]{1}[a-z]+$', nombre):
                                    data[0]['nombreZona'] = nombre                              
                            if opcion == 2:
                                totalCapacidad = input('Ingrese la nueva capacidad máxima de la zona en Campuslands => ')
                                if totalCapacidad.isdigit():
                                    totalCapacidad = int(totalCapacidad)
                                    data[0]['totalCapacidad'] = totalCapacidad

                                    # peticion = requests.put(f"http://154.38.171.54:5502/zonas/{id}", data=json.dumps(data[0]).encode("UTF-8"))
                                    # res = peticion.json()
                                    # res['Mensaje'] = '\nEl dato fue editado satisfactoriamente'
                                    # print()
                                    # print(res['Mensaje'])
                                    # input('\nPresione la tecla Enter para poder continuar...')
                                    # return [res]
                                
                        elif opcion == 2:
                            break
                        else:
                            raise Exception ('---> El dato ingresado debe ser 1 o 2 ')
                else:
                    raise Exception ('---> El dato ingresado debe ser 1 o 2 ')     

                peticion = requests.put(f"http://154.38.171.54:5502/zonas/{id}", data=json.dumps(data[0]).encode("UTF-8"))
                res = peticion.json()
                res['Mensaje'] = '\nEl dato fue editado satisfactoriamente'
                print()
                print(res['Mensaje'])
                input('\nPresione la tecla Enter para poder continuar...')
                return [res]   
            
            except Exception as error:
                print('---ERROR---')
                print(error)
                break





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
                        idedit = input('\nIngrese el ID de la zona en Campuslands que deseas editar => ')
                        editZonas(idedit)
                    if opcion == 3:
                        iddelete = input('\nIngrese el ID de la zona en Campuslands que deseas eliminar => ')
                        deleteZonas(iddelete)
                    # if opcion == 4:
                    #     searchZonas()
                    # if opcion == 5:
                    #     break

        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')