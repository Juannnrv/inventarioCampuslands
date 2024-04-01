import os
import json
import re
import requests
from tabulate import tabulate
import datetime
import shortuuid
import random
import modules.getActivos as gA

# Obtener la fecha actual
fecha_actual = datetime.date.today()

fecha_formateada = fecha_actual.strftime("%y-%m-%d")

def DataAsignaciones():
    result = []
    for val in gA.Activos():
        asignaciones = val.get("asignaciones", [])
        for asignacion in asignaciones:
            diccionario = {}
            diccionario["NroAsignacion"] = asignacion.get("NroAsignacion")
            diccionario["FechaAsignacion"] = asignacion.get("FechaAsignacion")
            diccionario["TipoAsignacion"] = asignacion.get("TipoAsignacion")
            diccionario["AsignadoA"] = asignacion.get("AsignadoA")
            diccionario["ID Activo"] = val.get("id")
            diccionario["Nombre del activo"] = val.get("Nombre")
            result.append(diccionario)
    return result
    
def NroAsiganciones(NroAsignacion):
    asignaciones_encontradas = []
    for val in DataAsignaciones():
        if val.get("NroAsignacion") == NroAsignacion:
            asignaciones_encontradas.append(val)
            return asignaciones_encontradas
    print('\nLa asignación no existe')
    return asignaciones_encontradas




def postAsignacionActivos():
    data = gA.Activos()
    
    while True:
        os.system('clear')
        print("""
        A continuación agregaras una nueva asignación a un activo existente en SISTEMA G&C DE INVENTARIO CAMPUSLANDS
        
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
                        idPost = input('\nIngrese el ID del activo en el cual deseas crear una asignación en SISTEMA G&C DE INVENTARIO CAMPUSLANDS => ')

                        # Validar la existencia del ID del activo
                        activo_encontrado = None
                        for activo in data:
                            if activo["id"] == idPost:
                                activo_encontrado = activo
                                historialActivos = activo.get('historialActivos', [])
                                
                                if len(historialActivos) > 0:
                                    ultimasignacion = historialActivos[-1]
                                    tipo = ultimasignacion['tipoMov']
                                else:
                                    tipo = None
                                break

                        if not activo_encontrado:
                            raise Exception('\n---> El ID del activo no existe')

                        # Validar el estado del activo y si se realizo un movimiento anteriormente
                        if activo_encontrado["idEstado"] != "0" and (tipo == "2" or tipo == "3"):
                            raise Exception('---> No se puede asignar un activo en reparación, dado de baja o ya asignado')
                        
                        print("""
                            ¿Se le asignó el activo a una Zona o Persona?
                            
                                            1. Zona
                                            2. Persona
                            """)
                        opcion = input('\nSeleccione una de las opciones => ')
                        if re.match(r'^[0-9]+$', opcion):
                            opcion = int(opcion)
                            if opcion == 1:
                                TipoAsignacion = 'Zona'
                            if opcion == 2:
                                TipoAsignacion = 'Personal'
                        else:
                            raise Exception('\n---> Tipo de asignación no válido')
                        
                        AsignadoA = input('\nIngresa el ID de la persona o zona a la cual le fue asignado el activo => ')
                        if not re.match(r'^[0-9a-z]+$', AsignadoA):
                            raise Exception('\n---> ID de asignación no válido')

                        activo_encontrado["asignaciones"].append({"NroAsignacion": shortuuid.random(length=4), "FechaAsignacion": fecha_formateada, "TipoAsignacion": TipoAsignacion, "AsignadoA": AsignadoA})
                        
                        try:
                            activo_encontrado["idEstado"] = "1"
                            headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
                            peticion = requests.put(f'http://154.38.171.54:5502/activos/{idPost}', headers=headers, data=json.dumps(activo_encontrado, indent=4))
                            res = peticion.json()
                            res['Mensaje'] = '\nAsignación creada satisfactoriamente'
                            print(res['Mensaje'])  
                            input('\nPresione Enter para continuar...')
                            break
                        except Exception as error:
                            print('\n---ERROR---')
                            print(error)
                            input('\nPresione Enter para continuar...')
                            break
                        
                    elif opcion == 2:
                        break
                        
            else:
                raise Exception ('---> El dato ingresado debe ser 1 o 2')
                        
        except Exception as error:
            print('\n---ERROR---')
            print(error)
            input('\nPresione Enter para continuar...')






def menuAsignacionActivos():
    while True:
        os.system('clear')
        print('''
                        
                            --- MENÚ ASIGNACIÓN ACTIVOS ---
                        

                            1. 🪄  Crear asignación
                            
                            2. 🗂️  Buscar asignación
                            
                            
                            3. Regresar al menú principal
''')
        try:
            opcion = input('\nSeleccione una de las opciones => ')
            if re.match(r'^[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion >= 1 and opcion <= 3:
                    if opcion == 1:
                        postAsignacionActivos()
                    elif opcion == 2:
                        NroAsignacion = input('\nIngrese el número de asignación del activo el cual deseas buscar una asignación en SISTEMA G&C DE INVENTARIO CAMPUSLANDS => ')
                        print()
                        print(tabulate(NroAsiganciones(NroAsignacion), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresione Enter para continuar...')
                    elif opcion == 3:
                        break
        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')