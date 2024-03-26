import os
import json
import re
import requests

def Activos():
    # http://154.38.171.54:5502/activos
    peticion = requests.get('http://154.38.171.54:5502/activos')
    data = peticion.json()
    return data

def ActivosNroItem(NroItem):
    for val in Activos():
        if val.get('NroItem') == NroItem:
            return [val]

def postActivos():
    Activos = {}

    while True:
        os.system('clear')
        print("""
        A continuación agregaras un nuevo activo al inventario de Campuslands
        
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
                                    print("""
                                        ¿Desea asignarle el número de serial a su activo?
                                
                                                        1. Si
                                                        2. No
                                    """)
                                    opcion = input('\nSeleccione una de las opciones => ')
                                    try:
                                        if re.match(r'[0-9]+$', opcion):
                                            opcion = int(opcion)
                                            if opcion >= 1 and opcion <= 2:
                                                if opcion == 1:
                                                    NroSerial = input('Ingrese la número del serial asignado al activo => ')
                                                    if re.match(r'^[a-zA-Z0-9\s-]+$', NroSerial):
                                                        Activos['NroSerial'] = NroSerial
                                                elif opcion == 2:
                                                    Activos['NroSerial'] = 'Sin serial ' 
                                    except KeyboardInterrupt:
                                        print()
                                # NroSerial = input('Ingrese la número del serial asignado al activo => ')
                                # if re.match(r'^[A-Z0-9]+$', NroSerial):
                                #     Activos['NroSerial'] = NroSerial
                                            
                                CodCampus = input('Ingrese el código de Campus asignado al activo => ')
                                if re.match(r'^[A-Z]{3}[0-9]{3}$', CodCampus):
                                    Activos['CodCampus'] = CodCampus

                                NroFormulario = input('Ingrese el número de formulario asignado al activo => ')
                                if NroFormulario.isdigit():
                                    NroFormulario = int(NroFormulario)
                                    Activos['NroFormulario'] = NroFormulario

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
                                opcion = input('Ingrese el id de la marca asignado al activo => ')
                                try:
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
                                except KeyboardInterrupt:
                                    print()

                                # Categoría
                                print("""
                                        Categorías
                
                                    1. Equipo de computo
                                    2. Electrodomestico
                                    3. Juego
                                        """)
                                opcion = input('Ingrese el id de la marca asignado al activo => ')
                                try:
                                    if re.match(r'[0-9]+$', opcion):
                                        opcion = int(opcion)
                                        if opcion >= 1 and opcion <= 3:
                                            if opcion == 1:
                                                Activos['idCategoria'] = '1'
                                            elif opcion == 2:
                                                Activos['idCategoria'] = '2'
                                            elif opcion == 3:
                                                Activos['idCategoria'] = '3'
                                except KeyboardInterrupt:
                                    print()

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
                                try:
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
                                                

                                except KeyboardInterrupt:
                                    print()

                                ValorUnitario = input('Ingrese el valor unitario del activo => ')
                                if ValorUnitario.isdigit():
                                    Activos['ValorUnitario'] = ValorUnitario

                                # Estado
                                print("""
                                            Estados
                
                                    0. No asignado
                                    1. Asignado
                                    2. Dado de baja por daño
                                    3. En reparación y/o garantia
                                        """)
                                opcion = input('Ingrese el id asignado al estado de activo => ')
                                try:
                                    if re.match(r'[0-9]+$', opcion):
                                        opcion = int(opcion)
                                        if opcion >= 0 and opcion <= 2:
                                            if opcion == 0:
                                                Activos['idEstado'] = '0'
                                            elif opcion == 1:
                                                Activos['idEstado'] = '1'
                                            elif opcion == 2:
                                                Activos['idEstado'] = '2'
                                            elif opcion == 3:
                                                Activos['idEstado'] = '3'

                                    else:
                                        print('\nNo cumple con el formato esperado')
                                        break

                                except KeyboardInterrupt:
                                    print()
                                    break


                            except KeyboardInterrupt:
                                print('\nRegresando al menú principal...')
                                break

                    elif opcion == 2:
                        break 

        except Exception as error:
            print('---ERROR---')
            print(error)
            break
        
        Activos['historialActivos'] = []
        Activos['asignaciones'] = []

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5502/activos', headers=headers, data=json.dumps(Activos))
    res = peticion.json()
    res ['Mensaje'] = 'Activo guardado satisfactoriamente'
    return [res]
                        
    

# def deleteActivos():

# def editActivos():

# def searchAsignacionActivos():
        #Para obtener un activo específico por su ID: GET /activos/{id}









def menuActivos():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ ACTIVOS---

                        1. Agregar
                        2. Editar
                        3. Eliminar
                        4. Buscar
                        5. Regresar al menù principal
''')
        try:
            opcion = (input('\n Seleccione una de las opciones => '))
            if(re.match(r'[0-9]+$', opcion) is not None):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 5:
                    if opcion == 1:
                        postActivos()
                    elif opcion == 2:
                        deleteActivos()
                    elif opcion == 3:
                        editActivos()
                    elif opcion == 4:
                        searchActivos()
                    elif opcion == 5:
                        break
                    
        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')
                    

                    
