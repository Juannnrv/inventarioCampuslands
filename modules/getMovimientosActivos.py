import os
import json
import re
import requests
import modules.getActivos as gA
import modules.getPersonal as gP
import datetime
import shortuuid
import random
from tabulate import tabulate

# Obtener la fecha actual
fecha_actual = datetime.date.today()

fecha_formateada = fecha_actual.strftime("%y-%m-%d")

def retornarActivo(id):
    # Obtener la información del activo con el ID proporcionado
    data = gA.ActivosId(id)
    if data:
        if data[0]["idEstado"] != "0":
            while True:
                    os.system('clear')
                    print("""
                    A continuación retornarás un activo en SISTEMA G&C DE INVENTARIO CAMPUSLANDS
                    
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
                                    
                                    añadirhistorial = {}
                                    idRespMov = input('\nIngrese el ID de la persona responsable del movimiento => ')
                                    if gP.PersonasID(idRespMov):
                                        añadirhistorial["NroId"] = shortuuid.random(length=4)
                                        añadirhistorial["fecha"] = fecha_formateada
                                        añadirhistorial["tipoMov"] = "0"  # Creamos el idTipo 0 para referirnos que el Activo fue RETORNADO
                                        añadirhistorial["idRespMov"] = idRespMov
                                        diccsolo = data[0]
                                        historialActivos = diccsolo["historialActivos"]
                                        historialActivos.append(añadirhistorial)
                                        data[0]['idEstado'] = "0"
                                        data[0]['asignaciones'] = []

                                        # Enviar la solicitud PUT para actualizar el activo
                                        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0]).encode("UTF-8"))
                                        res = peticion.json()
                                        if 'Mensaje' in res:
                                            print(res['Mensaje'])
                                        print('\Activo retornado satisfactoriamente...')
                                        return [res]
                                    else:
                                        raise Exception('\nID de la persona no encontrado...')

                                elif opcion == 2:
                                    break
                            else:
                                raise Exception('---> El dato ingresado debe ser 1 o 2')
                        else:
                            raise Exception('---> El dato ingresado debe ser 1 o 2') 
                        
                    except Exception as error:
                        print('\n---ERROR---')
                        print(error)
                        break
        else:
            print('\nEl activo ya se encuentra en estado no asignado...')
            input('\nPresiona la tecla Enter para poder continuar...')

def dardebaja():
    # Obtener la información del activo con el ID proporcionado
    data = gA.ActivosId(id)
    if data:
        if data[0]["idEstado"] == "0": # NO SE PUEDE DAR DE BAJA UN ACTIVO QUE ESTE ASIGNADO
            while True:
                    os.system('clear')
                    print("""
                    A continuación retornarás un activo en SISTEMA G&C DE INVENTARIO CAMPUSLANDS
                    
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
                                    
                                    añadirhistorial = {}
                                    idRespMov = input('\nIngrese el ID de la persona responsable del movimiento => ')
                                    if gP.PersonasID(idRespMov):
                                        añadirhistorial["NroId"] = shortuuid.random(length=4)
                                        añadirhistorial["fecha"] = fecha_formateada
                                        añadirhistorial["tipoMov"] = "2" 
                                        añadirhistorial["idRespMov"] = idRespMov
                                        diccsolo = data[0]
                                        historialActivos = diccsolo["historialActivos"]
                                        historialActivos.append(añadirhistorial)
                                        data[0]['idEstado'] = "0"
                                        data[0]['asignaciones'] = []

                                        # Enviar la solicitud PUT para actualizar el activo
                                        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0]).encode("UTF-8"))
                                        res = peticion.json()
                                        if 'Mensaje' in res:
                                            print(res['Mensaje'])
                                        print('\Activo retornado satisfactoriamente...')
                                        return [res]
                                    else:
                                        raise Exception('\nID de la persona no encontrado...')

                                elif opcion == 2:
                                    break
                            else:
                                raise Exception('---> El dato ingresado debe ser 1 o 2')
                        else:
                            raise Exception('---> El dato ingresado debe ser 1 o 2') 
                        
                    except Exception as error:
                        print('\n---ERROR---')
                        print(error)
                        break
        else:
            print('\nEl activo se encuentra asignado...')
            input('\nPresiona la tecla Enter para poder continuar...')












def menuMovimientoActivos():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ MOVIMIENTOS DE ACTIVOS---

                            1. Retorno de activo
                            2. Dar de baja activo
                            3. Cambiar asignación de activo
                            4. Enviar a garantía de activo
                            5. Regresar al menù principal
''')
        try:
            opcion = (input('\n Seleccione una de las opciones => '))
            if(re.match(r'[0-9]+$', opcion) is not None):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 5:
                    if opcion == 1:
                        idretorno = input('\nIngresa el ID del activo que desea retornar => ')
                        print()
                        print(tabulate(retornarActivo(idretorno), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresiona la tecla Enter para poder continuar...')
                    # elif opcion == 2:
                    #     deleteActivos()
                    # elif opcion == 3:
                    #     editActivos()
                    # elif opcion == 4:
                    #     searchActivos()
                    elif opcion == 5:
                        break
                    
        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')