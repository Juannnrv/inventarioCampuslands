import os
import json
import re
import requests
from tabulate import tabulate

def Activos():
    # http://154.38.171.54:5502/activos
    peticion = requests.get('http://154.38.171.54:5502/activos')
    data = peticion.json()
    return data

def ActivosNroItem(NroItem):
    for val in Activos():
        if val.get('NroItem') == NroItem:
            return [val]
        
def ActivosId(id):
    for val in Activos():
        if val.get('id') == id:
            return [val]

def postActivos():
    Activos = {}

    while True:
        os.system('clear')
        print("""
        A continuación agregaras un nuevo activo a SISTEMA G&C DE INVENTARIO CAMPUSLANDS
        
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
                        while True:
                            os.system('clear')
                            try:
                                if not Activos.get('NroItem'):
                                    while True:
                                        NumeroItem = input('Ingrese el número de item del activo => ')
                                        if NumeroItem.isdigit():
                                            NumeroItem = int(NumeroItem)
                                            data = ActivosNroItem(NumeroItem)
                                            if data:
                                                raise Exception('El número de item del activo ya existe')
                                            else:
                                                Activos['NroItem'] = NumeroItem
                                        else:
                                            raise Exception('---> El número de item del activo no cumple con el estandar establecido')
                                        break
                                
                                    CodTransaccion = input('Ingrese el código de transacción del activo => ')
                                    if CodTransaccion.isdigit():
                                        CodTransaccion = int(CodTransaccion)
                                        Activos['CodTransaccion'] = CodTransaccion

                                # Serial
                                if not Activos.get('NroSerial'):
                                    print("""
                                        ¿Desea asignarle el número de serial a su activo?
                                
                                                        1. Si
                                                        2. No
                                    """)
                                    opcion = input('\nSeleccione una de las opciones => ')
                                    try:
                                        if re.match(r'[A-Z0-9]+$', opcion):
                                            opcion = int(opcion)
                                            if opcion >= 1 and opcion <= 2:
                                                if opcion == 1:
                                                    NroSerial = input('Ingrese la número del serial asignado al activo => ')
                                                    if re.match(r'^[a-zA-Z0-9\s-]+$', NroSerial):
                                                        Activos['NroSerial'] = NroSerial
                                                elif opcion == 2:
                                                    Activos['NroSerial'] = 'Sin serial' 
                                    except KeyboardInterrupt:
                                        print()
                                # NroSerial = input('Ingrese la número del serial asignado al activo => ')
                                # if re.match(r'^[A-Z0-9]+$', NroSerial):
                                #     Activos['NroSerial'] = NroSerial

                                if not Activos.get('CodCampus'):            
                                    CodCampus = input('Ingrese el código de Campus asignado al activo => ')
                                    if re.match(r'^[A-Z]{3}[0-9]{3}$', CodCampus):
                                        Activos['CodCampus'] = CodCampus

                                    NroFormulario = input('Ingrese el número de formulario asignado al activo => ')
                                    if NroFormulario.isdigit():
                                        NroFormulario = int(NroFormulario)
                                        Activos['NroFormulario'] = NroFormulario

                                if not Activos.get('Nombre'):
                                    Nombre = input('Ingrese el nombre del activo => ')
                                    if re.match(r'^[a-zA-Z0-9\s-]+$', Nombre):
                                        Activos['Nombre'] = Nombre

                                    Proveedor = input('Ingrese el proveedor del activo => ')
                                    if re.match(r'[A-Za-z]+\s[A-Za-z\s]+$', Proveedor):
                                        Activos['Proveedor'] = Proveedor

                                    EmpresaResponsable = input('Ingrese el nombre de la empresa responsable del activo => ')
                                    if re.match(r'[A-Za-z]+$', EmpresaResponsable):
                                        Activos['EmpresaResponsable'] = EmpresaResponsable

                                # Marca
                                    print("""
                                                Marcas
                    
                                            1. LG
                                            2. Compumax
                                            3. Logitech
                                            4. Benq
                                            5. Asus
                                            6. Lenovo
                                            7. Hp 
                                            """)
                                    opcion = input('Ingrese la opción de la marca del activo => ')
                                    
                                    if re.match(r'[0-9]+$', opcion):
                                        opcion = int(opcion)
                                        if opcion >= 1 and opcion <= 7:
                                            if opcion == 1:
                                                Activos['idMarca'] = '1'
                                            elif opcion == 2:
                                                Activos['idMarca'] = '2'
                                            elif opcion == 3:
                                                Activos['idMarca'] = '3'
                                            elif opcion == 4:
                                                Activos['idMarca'] = '4'
                                            elif opcion == 5:
                                                Activos['idMarca'] = '5'
                                            elif opcion == 6:
                                                Activos['idMarca'] = '6'
                                            elif opcion == 7:
                                                Activos['idMarca'] = '7' 
                            
                                # Categoría
                                    print("""
                                            Categorías
                    
                                        1. Equipo de computo
                                        2. Electrodomestico
                                        3. Juego
                                            """)
                                    opcion = input('Ingrese el id de la marca asignado al activo => ')
                                    if re.match(r'[0-9]+$', opcion):
                                        opcion = int(opcion)
                                        if opcion >= 1 and opcion <= 3:
                                            if opcion == 1:
                                                Activos['idCategoria'] = '1'
                                            elif opcion == 2:
                                                Activos['idCategoria'] = '2'
                                            elif opcion == 3:
                                                Activos['idCategoria'] = '3'
                                
                                # Tipo
                                    print("""
                                            Tipos de Activos
                    
                                        1. Monitor
                                        2. Cpu
                                        3. Teclado
                                        4. Mouse
                                        5. Aire acondicionado
                                        6. Portatil
                                        7. Televisor
                                        8. Arcade 
                                            """)
                                    opcion = input('Ingrese el id asignado al tipo de activo => ')
                                    if re.match(r'[0-9]+$', opcion):
                                        opcion = int(opcion)
                                        if opcion >= 1 and opcion <= 8:
                                            if opcion == 1:
                                                Activos['idTipo'] = '1'
                                            elif opcion == 2:
                                                Activos['idTipo'] = '2'
                                            elif opcion == 3:
                                                Activos['idTipo'] = '3'
                                            elif opcion == 4:
                                                Activos['idTipo'] = '4'
                                            elif opcion == 5:
                                                Activos['idTipo'] = '5'
                                            elif opcion == 6:
                                                Activos['idTipo'] = '6'
                                            elif opcion == 7:
                                                Activos['idTipo'] = '7' 
                                            elif opcion == 8:
                                                Activos['idTipo'] = '8'
                                            

                                if not Activos.get('ValorUnitario'):
                                    ValorUnitario = input('Ingrese el valor unitario del activo => ')
                                    if ValorUnitario.isdigit():
                                        Activos['ValorUnitario'] = ValorUnitario

                                    else:  
                                        raise Exception ("Lo siento no cumple con el formato esperado.")
                                    break 

                                else:
                                    raise Exception ('\nNo cumple con el formato esperado')
                                    break

                            except KeyboardInterrupt:
                                print('\nRegresando al menú principal...')
                                break

                        break

                    elif opcion == 2:
                        break 

        except Exception as error:
            print('---ERROR---')
            print(error)
            break
        
    Activos['idEstado'] = "0"
    Activos['historialActivos'] = []
    Activos['asignaciones'] = []
    

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5502/activos', headers=headers, data=json.dumps(Activos, indent=4))
    res = peticion.json()
    res ['Mensaje'] = '\nActivo guardado satisfactoriamente'
    print(res['Mensaje'])
    input('\nPresione Enter para continuar...')
    return [res]

def editActivos(id):
    data = ActivosId(id)
    if len(data):
        while True:
            os.system('clear')
            print("""
            A continuación editaras un activo existente de SISTEMA G&C DE INVENTARIO CAMPUSLANDS
            
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
                    ¿Qué dato desea actualizar?

                    1. Número de Item
                    2. Código de transacción
                    3. Número de serial
                    4. Código Campus
                    5. Número de formulario
                    6. Nombre
                    7. Proveedor
                    8. Empresa responsable
                    9. Id de marca
                    10. Id de categoría
                    11. Id de tipo
                    12. Valor unitario
                    13. Id estado
                                """)
                            opcion = input('\nIngrese una de las opciones => ')
                            if re.match(r'[0-9]+$', opcion):
                                opcion = int(opcion)
                                if opcion >= 1 and opcion <= 14:
                                    if opcion == 1:
                                        NroItem = input('\nIngrese el nuevo número de item del activo => ')
                                        if re.match(r'[0-9]+$', NroItem):
                                            NroItem = int(NroItem)
                                            data[0]['NroItem'] = NroItem
                                    if opcion == 2:
                                        CodTransaccion = input('\nIngrese el código de transacción del activo => ')
                                        if CodTransaccion.isdigit():
                                            CodTransaccion = int(CodTransaccion)
                                            data[0]['CodTransaccion'] = CodTransaccion
                                    if opcion == 3:
                                        # Serial
                                        print("""
                                        ¿Desea asignarle un nuevo número de serial a un activo ya existente?
                                
                                                                1. Si
                                                                2. No
                                    """)
                                        opcion = input('\nSeleccione una de las opciones => ')
                                        try:
                                            if re.match(r'[A-Z0-9]+$', opcion):
                                                opcion = int(opcion)
                                                if opcion >= 1 and opcion <= 2:
                                                    if opcion == 1:
                                                        NroSerial = input('\nIngrese el nuevo número del serial asignado al activo => ')
                                                        if re.match(r'^[a-zA-Z0-9\s-]+$', NroSerial):
                                                            data[0]['NroSerial'] = NroSerial
                                                    elif opcion == 2:
                                                        data[0]['NroSerial'] = 'Sin serial ' 
                                                else:
                                                    print('\nPor favor, seleccione una opción válida (1 o 2)')
                                                    break
                                        except KeyboardInterrupt:
                                            print()
                                    if opcion == 4:
                                        CodCampus = input('\nIngrese el nuevo código de Campus que vas a asignar al activo => ')
                                        if re.match(r'^[A-Z]{3}[0-9]{3}$', CodCampus):
                                            data[0]['CodCampus'] = CodCampus
                                    if opcion == 5:
                                        NroFormulario = input('\nIngrese el nuevo número de formulario del activo => ')
                                        if re.match(r'[0-9]+$', NroFormulario):
                                            NroFormulario = int(NroFormulario)
                                            data[0]['NroFormulario'] = NroFormulario
                                    if opcion == 6:
                                        Nombre = input('\nIngrese el nuevo nombre del activo => ')
                                        if re.match(r'^[a-zA-Z0-9\s-]+$', Nombre):
                                            data[0]['Nombre'] = Nombre
                                    if opcion == 7:
                                        Proveedor = input('\nIngrese el nuevo proveedor del activo => ')
                                        if re.match(r'^[a-zA-Z0-9\s-]+$', Proveedor):
                                            data[0]['Proveedor'] = Proveedor
                                    if opcion == 8:
                                        EmpresaResponsable = input('\nIngrese la nueva empresa responsable del activo => ')
                                        if re.match(r'^[a-zA-Z0-9\s-]+$', EmpresaResponsable):
                                            data[0]['EmpresaResponsable'] = EmpresaResponsable
                                    if opcion == 9:
                                        print("""
                                                Marcas
                    
                                            1. LG
                                            2. Compumax
                                            3. Logitech
                                            4. Benq
                                            5. Asus
                                            6. Lenovo
                                            7. Hp 
                                            """)
                                        opcion = input('\nSeleccione la opción de la nueva marca del activo => ')
                                        try:
                                            if re.match(r'[0-9]+$', opcion):
                                                opcion = int(opcion)
                                                if opcion >= 1 and opcion <= 7:
                                                    if opcion == 1:
                                                        data[0]['idMarca'] = '1'
                                                    elif opcion == 2:
                                                        data[0]['idMarca'] = '2'
                                                    elif opcion == 3:
                                                        data[0]['idMarca'] = '3'
                                                    elif opcion == 4:
                                                        data[0]['idMarca'] = '4'
                                                    elif opcion == 5:
                                                        data[0]['idMarca'] = '5'
                                                    elif opcion == 6:
                                                        data[0]['idMarca'] = '6'
                                                    elif opcion == 7:
                                                        data[0]['idMarca'] = '7'
                                                    
                                                    else:
                                                        print('\nPor favor, seleccione una opción válida (1 o 7)')
                                                        break
                                        except KeyboardInterrupt:
                                            print()

                                    if opcion == 10:
                                        print("""
                                            Categorías
                    
                                        1. Equipo de computo
                                        2. Electrodomestico
                                        3. Juego
                                            """)
                                        opcion = input('\nSeleccione la opción de la nueva categoría del activo => ')
                                        try:
                                            if re.match(r'[0-9]+$', opcion):
                                                opcion = int(opcion)
                                                if opcion >= 1 and opcion <= 3:
                                                    if opcion == 1:
                                                        data[0]['idCategoria'] = '1'
                                                    elif opcion == 2:
                                                        data[0]['idCategoria'] = '2'
                                                    elif opcion == 3:
                                                        data[0]['idCategoria'] = '3'
                                                    else:
                                                        print('\nPor favor, seleccione una opción válida (1 o 3)')
                                                        break
                                        except KeyboardInterrupt:
                                            print()

                                    if opcion == 11:
                                        print("""
                                            Tipos de Activos
                    
                                        1. Monitor
                                        2. Cpu
                                        3. Teclado
                                        4. Mouse
                                        5. Aire acondicionado
                                        6. Portatil
                                        7. Televisor
                                        8. Arcade 
                                            """)
                                        opcion = input('\nSeleccione el tipo de activo => ')
                                        try:
                                            if re.match(r'[0-9]+$', opcion):
                                                opcion = int(opcion)
                                                if opcion >= 1 and opcion <= 8:
                                                    if opcion == 1:
                                                        data[0]['idTipoActivo'] = '1'
                                                    if opcion == 2:
                                                        data[0]['idTipoActivo'] = '2'
                                                    if opcion == 3:
                                                        data[0]['idTipoActivo'] = '3'
                                                    if opcion == 4:
                                                        data[0]['idTipoActivo'] = '4'
                                                    if opcion == 5:
                                                        data[0]['idTipoActivo'] = '5'
                                                    if opcion == 6:
                                                        data[0]['idTipoActivo'] = '6'
                                                    if opcion == 7:
                                                        data[0]['idTipoActivo'] = '7'
                                                    if opcion == 8:
                                                        data[0]['idTipoActivo'] = '8'
                                                    else:
                                                        print('\nPor favor, seleccione una opción válida (1 o 8)')
                                                        break
                                        except KeyboardInterrupt:
                                            print()
                                    if opcion == 12:
                                        ValorUnitario = input('\nIngrese el nuevo valor unitario del activo => ')
                                        if re.match(r'^[0-9]+$', ValorUnitario):
                                            data[0]['ValorUnitario'] = ValorUnitario
                                    if opcion == 13:
                                        print("""
                                            Estados de Activos
                    
                                        0. No asignado
                                        1. Asignado
                                        2. Dado de baja por daño
                                        3. En reparación y/o garantía 
                                            """)
                                        opcion = input('\nSeleccione el tipo de activo => ')
                                        try:
                                            if re.match(r'[0-9]+$', opcion):
                                                opcion = int(opcion)
                                                if opcion >= 0 and opcion <= 3:
                                                    if opcion == 0:
                                                        data[0]['idEstado'] = '0'
                                                    if opcion == 1:
                                                        data[0]['idEstado'] = '1'
                                                    if opcion == 2:
                                                        data[0]['idEstado'] = '2'
                                                    if opcion == 3:
                                                        data[0]['idEstado'] = '3'
                                                else:
                                                    print('\nPor favor, seleccione una opción válida (0 o 3)')
                                                    break

                                        except KeyboardInterrupt:
                                            print()
                                            
                                    else:
                                        print('\nNo cumple con el formato esperado')
                                        break

                            break

                        elif opcion == 2:
                            break
                        else:
                            print('\nPor favor, seleccione una opción válida (1 o 2)')
                            break

            except Exception as error:
                print('---ERROR---')
                print(error)
                break
    
    # Activos['historialActivos'] = []
    # Activos['asignaciones'] = [] 
            
    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0]).encode("UTF-8"))
    res = peticion.json()
    res['Mensaje'] = '\nDato editado satisfactoriamente'
    print(res['Mensaje'])
    input('\nPresione Enter para continuar...')
    return [res]

def deleteActivos(id): 
    # No se elimina solo se cambia el estado del activo a NO ASIGNADO

    data = ActivosId(id)
    if len(data):
        while True:
            os.system('clear')
            print("""
            A continuación eliminaras un activo existente de SISTEMA G&C DE INVENTARIO CAMPUSLANDS
            
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
                            data[0]['idEstado'] = "0"
                        if opcion == 2:
                            break
                    else:
                        raise Exception ('\nPor favor, seleccione una opción válida (1 o 2)')
                        break
                else:
                    raise Exception('\nPor favor, seleccione una opción válida 1 o 2')
                break

            except Exception as error:
                print('---ERROR---')
                print(error)
                break

    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0]).encode("UTF-8"))
    res = peticion.json()
    res['Mensaje'] = '\nDato eliminado satisfactoriamente'
    print(res['Mensaje'])
    input('\nPresione Enter para continuar...')
    return [res]


def menuActivos():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ ACTIVOS---

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
                        postActivos()
                    elif opcion == 2:
                        idActivo = input('\nIngrese el ID del activo que deseas editar => ')
                        print(tabulate(editActivos(idActivo), headers='keys', tablefmt='fancy_grid'))
                    elif opcion == 3:
                        idActivo = input('\nIngrese el ID del activo que deseas eliminar => ')
                        print(tabulate(deleteActivos(idActivo), headers='keys', tablefmt='fancy_grid'))
                    elif opcion == 4:
                        idActivo = input('\nIngrese el ID del activo que deseas buscar => ')
                        print()
                        print(tabulate(ActivosId(idActivo), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresiona la tecla Enter para continuar...')
                    elif opcion == 5:
                        break
                    
        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')
                    

                    
