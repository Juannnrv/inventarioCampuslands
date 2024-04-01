import re
import json
import os 
import requests
import modules.getActivos as gA
from tabulate import tabulate

def Zonas():
    peticion = requests.get('http://154.38.171.54:5502/zonas')
    data = peticion.json()
    return data

def ZonasID(id):
    idEncontrados = []
    for val in Zonas():
        if val.get('id') == id:
            idEncontrados.append(val)
            return idEncontrados
    print('\nID no encontrado')
    return idEncontrados

def postZonas():
    Zonas = {}
    while True:
        os.system('clear')
        print("""
        A continuación agregaras una nueva zona a SISTEMA G&C DE INVENTARIO CAMPUSLANDS
        
                                👾 ¿Deseas continuar? 👾
            
                                    1. ✅ Si
                                    2. ❌ No
""")
        opcion = input('\nSeleccione una de las opciones => ')
        try:
            if re.match(r'[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion >= 1 and opcion <= 2:
                    if opcion == 1:
                        
                        if not Zonas.get('nombreZona'):
                            nombreZona = input('\nIngrese el nombre de la zona en Campuslands => ')
                            if re.match(r'^[A-Z]{1}[a-z]+$', nombreZona):
                                Zonas['nombreZona'] = nombreZona

                            totalCapacidad = input('Ingrese la capacidad máxima de la zona en Campuslands => ')
                            if totalCapacidad.isdigit():
                                totalCapacidad = int(totalCapacidad)
                                Zonas['totalCapacidad'] = totalCapacidad

                            else:
                                raise Exception('---> El dato ingresado de la zona en Campuslands no cumple con el formato establecido')
                            
                        else:
                            raise Exception('---> El dato ingresado de la zona en Campuslands ya existe')
                    
                    if opcion == 2:
                        break

            headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
            peticion = requests.post('http://154.38.171.54:5502/zonas', headers=headers, data=json.dumps(Zonas, indent=4))
            res = peticion.json()
            res['Mensaje'] = '\nZona guardada satisfactoriamente'
            print(res['Mensaje'])  
            return [res]

        except Exception as error:
            print('\n\n---ERROR---')
            print(error)
            break

def deleteZonas(id):
    data = gA.Activos()
    
    for activo in data:
        if activo['idEstado'] == "1":
            
            asignaciones = activo.get('asignaciones', [])
            
            if len(asignaciones):
                ultimasignacion = asignaciones[-1]
                asigandoA = ultimasignacion['AsignadoA']
                tipo = ultimasignacion['TipoAsignacion']
                
                if tipo == 'Zona' and asigandoA == id:
                    print('\nEsta zona tiene asignado un activo y no puede ser eliminada.')
                    break
                else:
                    peticion = requests.delete(f'http://154.38.171.54:5502/zonas/{id}')
                    res = peticion.json()
                    res['Mensaje'] = 'Zona eliminada satisfactoriamente'
                    print()
                    print(res['Mensaje'])
                    input('\nPresiona la tecla Enter para poder continuar...')
                    return [res]

def editZonas(id):
    data = ZonasID(id)
    if len(data):
        while True:
            os.system('clear')
            print("""
            A continuación editaras un dato de una zona existente de SISTEMA G&C DE INVENTARIO CAMPUSLANDS
            
                                            👾 ¿Deseas continuar? 👾
                        
                                                1. ✅ Si
                                                2. ❌ No
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
                return [res]   
            
            except Exception as error:
                print('\n---ERROR---')
                print(error)
                break




def menuZonas():
    while True:
        os.system('clear')
        print('''
                        
                        --- MENÚ ZONAS ---
                        

                        1. 🪄  Agregar
                        
                        2. 🖌️  Editar
                        
                        3. 👻 Eliminar
                        
                        4. 🗂️  Buscar
                        
                        
                        5. Regresar al menú principal
''')
        try:
            opcion = (input('\n Seleccione una de las opciones => '))
            if re.match(r'[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 5:
                    if opcion == 1:
                        print(tabulate(postZonas(), headers='keys', tablefmt='fancy_grid'))
                        input('\nIngresa la tecla Enter para poder continuar...')
                    if opcion == 2:
                        idedit = input('\nIngrese el ID de la zona en Campuslands que deseas editar => ')
                        print()
                        print(tabulate(editZonas(idedit), headers='keys', tablefmt='fancy_grid'))
                        input('\nIngresa la tecla Enter para poder continuar...')
                    if opcion == 3:
                        while True:
                            os.system('clear')
                            print("""
                            A continuación eliminaras una zona existente de SISTEMA G&C DE INVENTARIO CAMPUSLANDS
                            
                                                        👾 ¿Deseas continuar? 👾
                                    
                                                            1. ✅ Si
                                                            2. ❌ No
                    """)
                            opcion = input('\nSeleccione una de las opciones => ')
                            try:
                                if re.match(r'[0-9]+$', opcion):
                                    opcion = int(opcion)
                                    if opcion >= 1 and opcion <= 2:
                                        if opcion == 1:
                                            iddelete = input('\nIngrese el ID de la zona en Campuslands que deseas eliminar => ')
                                            deleteZonas(iddelete)
                                        elif opcion == 2:
                                            break
                                    else:
                                        raise Exception ('---> El dato ingresado debe ser 1 o 2 ')
                                else:
                                    raise Exception ('---> El dato ingresado debe ser 1 o 2 ')        
                            except Exception as error:
                                print('\n---ERROR---')
                                print(error)
                                break
                    if opcion == 4:
                        idsearch = input('\nIngresa el ID de la zona en Campuslands que deseas buscar => ')
                        print()
                        print(tabulate(ZonasID(idsearch), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresiona la tecla Enter para poder continuar...')
                    if opcion == 5:
                        break

        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')