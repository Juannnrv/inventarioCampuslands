import os
import json
import re
import requests
import modules.getActivos as gA
from tabulate import tabulate

def Allactivos():
    Activos = []
    
    for val in gA.Activos():
        Activos.append({
            "NroItem": val.get('NroItem'),
            "CodTransaccion": val.get('CodTransaccion'),
            "NroSerial": val.get('NroSerial'),
            "CodCampus": val.get('CodCampus'),
            "NroFormulario": val.get('NroFormulario'),
            "Nombre": val.get('Nombre'),
            "Proveedor": val.get('Proveedor'),
            "EmpresaResponsable": val.get('EmpresaResponsable'),
            "idMarca": val.get('idMarca'),
            "idCategoria": val.get('idCategoria'),
            "idTipo": val.get('idTipo'),
            "ValorUnitario": val.get('ValorUnitario'),
            "idEstado": val.get('idEstado'),
            "id": val.get('id'),
            "historialActivos": [],
            "asignaciones": []
        })
    return Activos

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

def Allasignacioens():
        result = []
        for val in gA.Activos():
            asignaciones = val.get("asignaciones", [])
            for asignacion in asignaciones:
                diccionario = {}
                diccionario["ID Activo"] = val.get("id")
                diccionario["Nombre del activo"] = val.get("Nombre")
                diccionario["NroAsignacion"] = asignacion.get("NroAsignacion")
                diccionario["FechaAsignacion"] = asignacion.get("FechaAsignacion")
                diccionario["TipoAsignacion"] = asignacion.get("TipoAsignacion")
                diccionario["AsignadoA"] = asignacion.get("AsignadoA")
                result.append(diccionario)
        return result

def ActivosDadosDeBaja():
    peticion = requests.get('http://154.38.171.54:5502/activos?idEstado=2')
    data = peticion.json()
    return data

def listarHistorialMovimientoActivos():
    result = []
    for val in gA.Activos():
        historialActivos = val.get("historialActivos", [])
        for historial in historialActivos:
            diccionario = {}
            diccionario["NroId"] = historial.get("NroId")
            diccionario["Fecha"] = historial.get("Fecha")
            diccionario["idRespMov"] = historial.get("idRespMov")
            diccionario["ID Activo"] = val.get("id")
            diccionario["Nombre del activo"] = val.get("Nombre")
            result.append(diccionario)
    return result

def menuReportes():
    while True:
        os.system('clear')
        print('''
                        
                            --- MENÚ REPORTES ---
                        
                        
                    1. 🗒️  Listar todos los activos
                    
                    2. 🗒️  Listar activos por categoría
                    
                    3. 🗒️  Listar activos dados de baja por daño
                    
                    4. 🗒️  Listar activos y asignación
                    
                    5. 🗒️  Listar historial de mov. de activo
                    
                    
                    6. Regresar al menú  principal
''')
        try:
            opcion = input('\nSeleccione una de las opciones => ')
            if re.match(r'[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 6:
                    if opcion == 1:
                        print(tabulate(Allactivos(), headers='keys', tablefmt='fancy_grid'))
                        input('Presiona la tecla Enter para continuar...')
                    elif opcion == 2:
                        while True:
                            print(tabulate(CategoriasActivo(), headers='keys', tablefmt='fancy_grid'))
                            print("""
                            
                            
                                        ¿Deseas observar las demas categorias?
                                
                                                    1. ✅ Si
                                                    2. ❌ No
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
                                    else:
                                        print('\nSeleccione 1 o 2 ')
                                else:
                                    print('\nDebes ingresar números')
                            except KeyboardInterrupt:
                                print()
                    elif opcion == 3:
                        print(tabulate(ActivosDadosDeBaja(), headers='keys', tablefmt='fancy_grid'))
                        input('Presiona la tecla Enter para continuar...')
                    elif opcion == 4:
                        print(tabulate(Allasignacioens(), headers='keys', tablefmt='fancy_grid'))
                        input('Presiona la tecla Enter para continuar...')
                    elif opcion == 5:
                        print(tabulate(listarHistorialMovimientoActivos(), headers='keys', tablefmt='fancy_grid'))
                        input('Presiona la tecla Enter para continuar...')
                    elif opcion == 6:
                        break

        except KeyboardInterrupt:
            print('\nSeleccione una de las opciones => ')
            

