import os
import json
import re
import requests
import datetime
import shortuuid
import random
from tabulate import tabulate

# Obtener la fecha actual
fecha_actual = datetime.date.today()

fecha_formateada = fecha_actual.strftime("%y-%m-%d")

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
    idEncontrados = []
    for val in Activos():
        if val.get('id') == id:
            idEncontrados.append(val)
            return idEncontrados
    print('\nEl activo no existe')
    return idEncontrados

def postActivos():
    Activos = {}

    while True:
        os.system('clear')
        print("""
        A continuación agregaras un nuevo activo a SISTEMA G&C DE INVENTARIO CAMPUSLANDS
        
                                👾👾 ¿Deseas continuar? 👾👾
            
                                    1. ✅ Si
                                    
                                    2. ❌ No
""")
        opcion = input('\nSeleccione una de las opciones => ')
        try:
            if re.match(r'[0-9]+$', opcion):
                opcion = int(opcion)
                if opcion == 1:
                    while True:
                        try:
                            if not Activos.get('NroItem'):
                                while True:
                                    os.system('clear')
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
                            else:
                                raise Exception('---> El código de transacción del activo solo debe contener digitos')

                            if not Activos.get('NroSerial'):
                                print("""
                                    ¿Desea asignarle el número de serial a su activo?
                            
                                                    1. ✅ Si
                                                    2. ❌ No
                                """)
                                opcion = input('\nSeleccione una de las opciones => ')
                                try:
                                    if re.match(r'[A-Z0-9]+$', opcion):
                                        opcion = int(opcion)
                                        if opcion == 1:
                                            NroSerial = input('Ingrese el número del serial asignado al activo => ')
                                            if re.match(r'^[a-zA-Z0-9\s-]+$', NroSerial):
                                                Activos['NroSerial'] = NroSerial
                                        elif opcion == 2:
                                            Activos['NroSerial'] = 'Sin serial' 
                                        else:
                                            raise Exception ('---> El dato ingresado debe ser 1 o 2 ')
                                except KeyboardInterrupt:
                                    print()
                            
                            if not Activos.get('CodCampus'):            
                                CodCampus = input('Ingrese el código de Campus asignado al activo => ')
                                if re.match(r'^[A-Z]{3}[0-9]{3}$', CodCampus):
                                    Activos['CodCampus'] = CodCampus
                                else:
                                    raise Exception ('---> El código de Campus debe tener 3 letras y 3 números')

                                NroFormulario = input('Ingrese el número de formulario asignado al activo => ')
                                if NroFormulario.isdigit():
                                    NroFormulario = int(NroFormulario)
                                    Activos['NroFormulario'] = NroFormulario
                                else:
                                    raise Exception('---> El número de formulario del activo solo debe contener digitos')

                            if not Activos.get('Nombre'):
                                Nombre = input('Ingrese el nombre del activo => ')
                                if re.match(r'^[^\n]+$', Nombre):
                                    Activos['Nombre'] = Nombre
                                
                                Proveedor = input('Ingrese el proveedor del activo => ')
                                if re.match(r'[A-Za-z]+\s[A-Za-z\s]+$', Proveedor):
                                    Activos['Proveedor'] = Proveedor

                                EmpresaResponsable = input('Ingrese el nombre de la empresa responsable del activo => ')
                                if re.match(r'[A-Za-z]+$', EmpresaResponsable):
                                    Activos['EmpresaResponsable'] = EmpresaResponsable

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
                                        Activos['idMarca'] = str(opcion)
                                    else:
                                        raise Exception ('---> El dato ingresado debe ser un número del 1 al 7')
                            
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
                                        Activos['idCategoria'] = str(opcion)
                                    else:
                                        raise Exception ('---> El dato ingresado debe ser un número del 1 al 3')
                            
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
                                        Activos['idTipo'] = str(opcion)
                                    else:
                                        raise Exception ('---> El dato ingresado debe ser un número del 1 al 8')
                                        
                            if not Activos.get('ValorUnitario'):
                                ValorUnitario = input('Ingrese el valor unitario del activo => ')
                                if ValorUnitario.isdigit():
                                    Activos['ValorUnitario'] = ValorUnitario
                                    break
                                else:
                                    raise Exception('---> El valor unitario del activo solo debe contener digitos')
                                
                        except KeyboardInterrupt:
                            print('\nRegresando al menú principal...')
                            break
                    break
                elif opcion == 2:
                    break 
                else:
                    raise Exception ('---> El dato ingresado debe ser 1 o 2')
        
        except Exception as error:
            print('\n---ERROR---')
            print(error)
            input('\nPresiona Enter para continuar...')
            continue
        
    Activos['idEstado'] = "0"
    Activos['historialActivos'] = []
    Activos['asignaciones'] = []
    
    try:
        
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
        peticion = requests.post('http://154.38.171.54:5502/activos', headers=headers, data=json.dumps(Activos, indent=4))
        res = peticion.json()
        res ['Mensaje'] = '\nActivo guardado satisfactoriamente'
        print(res['Mensaje'])
        return [res]
    
    except Exception as error:
            print('\n---ERROR---')
            input('\nPresiona Enter para continuar...')
            print(error)


def editActivos(id):
    data = ActivosId(id)
    if not data:
        print("El activo no existe.")
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
        print("""
        A continuación editarás un activo existente de SISTEMA G&C DE INVENTARIO CAMPUSLANDS
            
                                👾 ¿Deseas continuar? 👾
                
                                    1. ✅ Si
                                    2. ❌ No
        """)
        opcion = input('\nSeleccione una de las opciones => ')

        if opcion == '1':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
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

                if opcion.isdigit():
                    opcion = int(opcion)
                    if opcion >= 1 and opcion <= 13:
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
                            if opcion == 1:
                                NroItem = input('\nIngrese el nuevo número de item del activo => ')
                                if NroItem.isdigit():
                                    data[0]['NroItem'] = int(NroItem)
                                    break
                                else:
                                    print('---> El número de item debe contener solo dígitos.')
                            elif opcion == 2:
                                # Código de transacción
                                CodTransaccion = input('\nIngrese el código de transacción del activo => ')
                                if CodTransaccion.isdigit():
                                    data[0]['CodTransaccion'] = int(CodTransaccion)
                                    break
                                else:
                                    print('---> El código de transacción debe contener solo dígitos.')
                            elif opcion == 3:
                                print("""
                                ¿Desea asignarle un nuevo número de serial a un activo ya existente?
        
                                                        1. ✅ Si
                                                        2. ❌ No
                                """)
                                opcion_serial = input('\nSeleccione una de las opciones => ')
                                if opcion_serial == '1':
                                    NroSerial = input('\nIngrese el nuevo número del serial asignado al activo => ')
                                    if re.match(r'^[a-zA-Z0-9\s-]+$', NroSerial):
                                        data[0]['NroSerial'] = NroSerial
                                        break
                                    else:
                                        print('---> El formato del número de serial no es válido.')
                                elif opcion_serial == '2':
                                    data[0]['NroSerial'] = 'Sin serial'
                                    break
                                else:
                                    print('---> Opción no válida.')
                            elif opcion == 4:
                                CodCampus = input('\nIngrese el nuevo código de Campus que vas a asignar al activo => ')
                                if re.match(r'^[A-Z]{3}[0-9]{3}$', CodCampus):
                                    data[0]['CodCampus'] = CodCampus
                                    break
                                else:
                                    print('---> El código de Campus debe tener 3 letras y 3 números')
                            elif opcion == 5:
                                NroFormulario = input('\nIngrese el nuevo número de formulario del activo => ')
                                if NroFormulario.isdigit():
                                    data[0]['NroFormulario'] = int(NroFormulario)
                                    break
                                else:
                                    print('---> El número de formulario del activo solo debe contener dígitos')
                            elif opcion == 6:
                                Nombre = input('\nIngrese el nuevo nombre del activo => ')
                                if re.match(r'^[^\n]+$', Nombre):
                                    data[0]['Nombre'] = Nombre
                                    break
                                else:
                                    print('---> El formato del nombre no es válido.')
                            elif opcion == 7:
                                Proveedor = input('\nIngrese el nuevo proveedor del activo => ')
                                if re.match(r'^[a-zA-Z0-9\s-]+$', Proveedor):
                                    data[0]['Proveedor'] = Proveedor
                                    break
                                else:
                                    print('---> El formato del proveedor no es válido.')
                            elif opcion == 8:
                                EmpresaResponsable = input('\nIngrese la nueva empresa responsable del activo => ')
                                if re.match(r'^[a-zA-Z0-9\s-]+$', EmpresaResponsable):
                                    data[0]['EmpresaResponsable'] = EmpresaResponsable
                                    break
                                else:
                                    print('---> El formato de la empresa responsable no es válido.')
                            elif opcion == 9:
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
                                opcion_marca = input('\nSeleccione la opción de la nueva marca del activo => ')
                                if opcion_marca.isdigit():
                                    opcion_marca = int(opcion_marca)
                                    if opcion_marca >= 1 and opcion_marca <= 7:
                                        data[0]['idMarca'] = str(opcion_marca)
                                        break
                                    else:
                                        print('---> Opción no válida.')
                                else:
                                    print('---> Por favor, ingrese un número.')
                            elif opcion == 10:
                                print("""
                                    Categorías
        
                                1. Equipo de computo
                                2. Electrodomestico
                                3. Juego
                                    """)
                                opcion_categoria = input('\nSeleccione la opción de la nueva categoría del activo => ')
                                if opcion_categoria.isdigit():
                                    opcion_categoria = int(opcion_categoria)
                                    if opcion_categoria >= 1 and opcion_categoria <= 3:
                                        data[0]['idCategoria'] = str(opcion_categoria)
                                        break
                                    else:
                                        print('---> Opción no válida.')
                                else:
                                    print('---> Por favor, ingrese un número.')
                            elif opcion == 11:
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
                                opcion_tipo = input('\nSeleccione el tipo de activo => ')
                                if opcion_tipo.isdigit():
                                    opcion_tipo = int(opcion_tipo)
                                    if opcion_tipo >= 1 and opcion_tipo <= 8:
                                        data[0]['idTipoActivo'] = str(opcion_tipo)
                                        break
                                    else:
                                        print('---> Opción no válida.')
                                else:
                                    print('---> Por favor, ingrese un número.')
                            elif opcion == 12:
                                ValorUnitario = input('\nIngrese el nuevo valor unitario del activo => ')
                                if ValorUnitario.isdigit():
                                    data[0]['ValorUnitario'] = ValorUnitario
                                    break
                                else:
                                    print('---> El valor unitario del activo solo debe contener dígitos')
                            elif opcion == 13:
                                print("""
                                    Estados de Activos
        
                                0. No asignado
                                1. Asignado
                                2. Dado de baja por daño
                                3. En reparación y/o garantía 
                                    """)
                                opcion_estado = input('\nSeleccione el tipo de activo => ')
                                if opcion_estado.isdigit():
                                    opcion_estado = int(opcion_estado)
                                    if opcion_estado >= 0 and opcion_estado <= 3:
                                        data[0]['idEstado'] = str(opcion_estado)
                                        break
                                    else:
                                        print('---> Opción no válida.')
                                else:
                                    print('---> Por favor, ingrese un número.')

                        try:
                            peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0]).encode("UTF-8"))
                            res = peticion.json()
                            res['Mensaje'] = '\nDato editado satisfactoriamente...'
                            if 'Mensaje' in res:
                                print(res['Mensaje'])
                            return [res]
                        except Exception as error:
                            print('\n---ERROR---')
                            print(error)
                    else:
                        print('---> El dato ingresado debe ser un número del 1 al 13')
                else:
                    print('---> Por favor, ingrese un número válido.')
            break
        elif opcion == '2':
            print('\nRegresando al menú de Activos...')
            break
        else:
            print('---> El dato ingresado debe ser 1 o 2')

    
    # Activos['historialActivos'] = []
    # Activos['asignaciones'] = [] 


def deleteActivos(id): 
    # No se elimina solo se cambia el estado del activo a NO ASIGNADO

    data = ActivosId(id)
    if len(data):
        while True:
            os.system('clear')
            print("""
            A continuación eliminaras un activo existente de SISTEMA G&C DE INVENTARIO CAMPUSLANDS
            
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
                            if len(data[0]['asignaciones']) == 0:
                                data[0]['idEstado'] = "0"
                                
                                añadirhistorial = {}
                                añadirhistorial["NroId"] = shortuuid.random(length=4)
                                añadirhistorial["fecha"] = fecha_formateada
                                añadirhistorial["tipoMov"] = "2"  
                                añadirhistorial["idRespMov"] = "1"
                                diccsolo = data[0]
                                historialActivos = diccsolo["historialActivos"]
                                historialActivos.append(añadirhistorial)
                                data[0]['asignaciones'] = []
                            else:
                                raise Exception('El activo está asignado a una persona o zona y no se puede eliminar.')
                        if opcion == 2:
                            break
                    else:
                        raise Exception('\nPor favor, seleccione una opción válida (1 o 2)')
                else:
                    raise Exception('\nPor favor, seleccione una opción válida (1 o 2)')
                break

            except Exception as error:
                print('\n---ERROR---')
                print(error)
                break

    try:
        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0]).encode("UTF-8"))
        res = peticion.json()
        if 'Mensaje' in res:
            print(res['Mensaje'])
        print('\nDato eliminado satisfactoriamente')
        input('\nPresione Enter para continuar...')
        return [res]
    except Exception as error:
        print('\n---ERROR---')
        print(error)




def menuActivos():
    while True:
        os.system('clear')
        print('''
                        
                        --- MENÚ ACTIVOS ---
                        
                        
                        1. 🪄  Agregar
                        
                        2. 🖌️  Editar
                        
                        3. 👻 Eliminar
                        
                        4. 🗂️  Buscar
                        
                        
                        5. Regresar al menú principal
''')
        try:
            opcion = (input('\n Seleccione una de las opciones => '))
            if(re.match(r'[0-9]+$', opcion) is not None):
                opcion = int(opcion)
                if opcion >= 0 and opcion <= 5:
                    if opcion == 1:
                        print(tabulate(postActivos(), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresiona la tecla Enter para continuar...')
                    elif opcion == 2:
                        idActivo = input('\nIngrese el ID del activo que deseas editar => ')
                        print(tabulate(editActivos(idActivo), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresiona la tecla Enter para continuar...')
                    elif opcion == 3:
                        idActivo = input('\nIngrese el ID del activo que deseas eliminar => ')
                        deleteActivos(idActivo)
                    elif opcion == 4:
                        idActivo = input('\nIngrese el ID del activo que deseas buscar => ')
                        print()
                        print(tabulate(ActivosId(idActivo), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresiona la tecla Enter para continuar...')
                    elif opcion == 5:
                        break
                    
        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')