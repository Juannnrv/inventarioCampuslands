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
                                        nombre = input('Ingrese el nombre de la zona en Campuslands => ')
                                        if re.match(r'^[A-Z]{1}[a-z]+$', nombre):
                                            Zonas['nombreZona'] = nombre

                                        capacidad = input('Ingrese la capacidad máxima de la zona en Campuslands => ')
                                        if capacidad.isdigit():
                                            capacidad = int(capacidad)
                                            Zonas['capacidad'] = capacidad
                                            
                                            headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
                                            peticion = requests.post('http://154.38.171.54:5502/zonas', headers=headers, data=json.dumps(Zonas, indent=4))
                                            res = peticion.json()
                                            res['Mensaje'] = 'Zona guardada satisfactoriamente'
                                            print(res['Mensaje'])  # Mostrar el mensaje aquí
                                            input('Presione Enter para continuar...')
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

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
        peticion = requests.post('http://154.38.171.54:5502/zonas', headers=headers, data=json.dumps(Zonas, indent=4))
        res = peticion.json()
        res ['Mensaje'] = 'Zona guardada satisfactoriamente'
        return [res]


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