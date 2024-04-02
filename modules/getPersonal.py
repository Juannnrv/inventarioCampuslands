import re
import json
import os 
import requests
import modules.getActivos as gA
from tabulate import tabulate

# http://154.38.171.54:5502/personas

def Personas():
    peticion = requests.get('http://154.38.171.54:5502/personas')
    data = peticion.json()
    return data

def PersonasID(id):
    idEncontrados = []
    for val in Personas():
        if val.get('id') == id:
            idEncontrados.append(val)
            return idEncontrados
    print('\nID no encontrado')
    return idEncontrados

def postPersonal():
    personas = {}
    
    while True:
        os.system('clear')
        print("""
        A continuación agregaras una nueva persona a SISTEMA G&C DE INVENTARIO CAMPUSLANDS
        
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
                        while True:
                            os.system('clear')

                            if 'nroId (CC, Nit)' not in personas:
                                nroId = input('\nIngrese la Cc o Nit de la persona => ')
                                if nroId.isdigit():
                                    personas['nroId (CC, Nit)'] = nroId
                                else:
                                    raise Exception('---> La Cc o Nit de la persona no cumple, debes ingresar números')
                                
                            if 'Nombre' not in personas:
                                nombre = input('Ingrese el nombre de la persona => ')
                                if re.match(r'^[a-zA-Z\s-]+$', nombre):
                                    personas['Nombre'] = nombre
                                else:
                                    raise Exception('---> El nombre de la persona no cumple, debes ingresar letras')
                                
                            if 'Email' not in personas:
                                email = input('Ingrese el email de la persona => ')
                                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$', email):
                                    personas['Email'] = email
                                else:
                                    raise Exception('---> El email de la persona no cumple con el estandar establecido')
                                
                            if 'Telefonos' not in personas:
                                personas['Telefonos'] = []  # Si la lista de teléfonos no existe, créala

                                #MOVIL
                                # Solicitar al usuario el ID y el número de teléfono móvil
                                movil_id = input('\nIngrese el ID del móvil de la persona => ')
                                movil_num = input('Ingrese el número de móvil de la persona => ')

                                # Verificar que el ID y el número de teléfono móvil sean dígitos
                                if movil_id.isdigit() and movil_num.isdigit():

                                    # Agregar el número de teléfono móvil a la lista 'Telefonos' con la estructura correcta
                                    personas['Telefonos'].append({"movil": {"id": movil_id, "num": movil_num}})
                                else:
                                    raise Exception('---> El ID y el número de móvil deben contener solo dígitos.')
                                
                                # CASA
                                casa_id = input('\nIngrese el ID del número asignado a la casa de la persona => ')
                                casa_num = input('Ingrese el número de la casa de la persona => ')
                                if casa_id.isdigit() and casa_num.isdigit():
                                    personas['Telefonos'].append({"casa": {"id": casa_id, "num": casa_num}})
                                else:
                                    raise Exception('---> El ID y el número de móvil deben contener solo dígitos.')
                                
                                #PERSONAL
                                personal_id = input('\nIngresa el ID del número personal => ')
                                personal_num = input('Ingrese el número personal => ')
                                if personal_id.isdigit() and personal_num.isdigit():
                                    personas['Telefonos'].append({"personal": {"id": personal_id, "num": personal_num}})
                                else:
                                    raise Exception('---> El ID y el número de móvil deben contener solo dígitos.')
                                
                                #OFICINA
                                oficina_id = input('\nIngrese el ID asignado a la oficina de la persona => ')
                                oficina_num = input('Ingrese el número asignado a la oficina de la persona => ')
                                if oficina_id.isdigit() and oficina_num.isdigit():
                                    personas['Telefonos'].append({"oficina": {"id": oficina_id, "num": oficina_num}})
                                else:
                                    raise Exception('---> El ID y el número de móvil deben contener solo dígitos.')
                                
                                headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
                                peticion = requests.post('http://154.38.171.54:5502/personas', headers=headers, data=json.dumps(personas, indent=4))
                                res = peticion.json()
                                res ['Mensaje'] = '\nPersona guardada satisfactoriamente'
                                print(res['Mensaje'])
                                input('\nPresione Enter para continuar...')
                                return [res]
                            
                            break

                elif opcion == 2:
                    break

            else:
                raise Exception ('---> El dato ingresado debe ser 1 o 2 ')
            
        except Exception as error:
            print('\n---ERROR---')
            print(error)
            break

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5502/personas', headers=headers, data=json.dumps(personas, indent=4))
    res = peticion.json()
    res ['Mensaje'] = '\nPersona guardada satisfactoriamente'
    print(res['Mensaje'])
    input('\nPresione Enter para continuar...')
    return [res]

def deletePersonal(id):
    data = gA.Activos()
    
    for activo in data:
        if activo['idEstado'] == "1":
            
            asignaciones = activo.get("asignaciones", [])
            if len(asignaciones):
                ultimasignacion = asignaciones[-1]
                asignado = ultimasignacion["AsignadoA"]
                tipo = ultimasignacion['TipoAsignacion'] 
                
                if tipo == "Personal" and asignado == id:
                    print('\nEsta persona tiene asignado un activo y no puede ser eliminada.')
                    break
                else:
                    peticion_persona = requests.delete(f'http://154.38.171.54:5502/personas/{id}')
                    data = peticion_persona.json()
                    data['Mensaje'] = '\nPersona eliminada satisfactoriamente'
                    print(data['Mensaje'])
                    input('\nPresione Enter para continuar...')

def editPersonal(id):
    
    data = PersonasID(id)
    if len(data):
        while True:
            os.system('clear')
            print("""
            A continuación editaras un activo existente de SISTEMA G&C DE INVENTARIO CAMPUSLANDS
            
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
                    ¿Qué dato desea actualizar?

                    1. Número de ID (CC, Nit)
                    2. Nombre 
                    3. Email
                    
                    ---Telefonos---
                    
                    => Movil
                    4. ID
                    5. Número 
                    
                    => Casa
                    6. ID
                    7. Número
                    
                    => Personal
                    8. ID
                    9. Número
                    
                    => Oficina
                    10. ID
                    11. Número
                                """)
                            opcion = input('\nIngrese una de las opciones => ')
                            if re.match(r'[0-9]+$', opcion):
                                opcion = int(opcion)
                                if opcion >= 1 and opcion <= 11:
                                    if opcion == 1:
                                        nroId = input('\nIngrese la nueva Cc o Nit de la persona => ')
                                        if nroId.isdigit():
                                            data[0]['nroId (CC, Nit)'] = nroId
                                        else:
                                            raise Exception('---> La Cc o Nit de la persona no cumple, debes ingresar números')
                                    if opcion == 2:
                                        nombre = input('\nIngrese el nombre de la persona => ')
                                        if re.match(r'^[a-zA-Z0-9\s-]+$', nombre):
                                            data[0]['Nombre'] = nombre
                                        else:
                                            raise Exception('---> El nombre de la persona no cumple, debes ingresar letras')
                                    if opcion == 3:
                                        email = input('\nIngrese el email de la persona => ')
                                        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$', email):
                                            data[0]['Email'] = email
                                            
                                    if opcion == 4:
                                        movil_id = input('\nIngrese el nuevo ID del móvil de la persona => ')
                                        if movil_id.isdigit():
                                            data[0]['Telefonos'][0]['movil']['id'] = movil_id
                                        else:
                                            raise Exception('---> El ID debe contener solo dígitos.')
                                    if opcion == 5:
                                        movil_num = input('Ingrese el número del móvil de la persona => ')
                                        if movil_num.isdigit():
                                            data[0]['Telefonos'][0]['movil']['num'] = movil_num
                                        else:
                                            raise Exception('---> El número debe contener solo dígitos.')
                                    if opcion == 6:
                                        casa_id = input('\nIngrese el ID de la casa de la persona => ')
                                        if casa_id.isdigit():
                                            data[0]['Telefonos'][1]['casa']['id'] = casa_id
                                        else:
                                            raise Exception('---> El ID debe contener solo dígitos.')
                                    if opcion == 7:
                                        casa_num = input('Ingrese el número de casa de la persona => ')
                                        if casa_num.isdigit():
                                            data[0]['Telefonos'][1]['casa']['num'] = casa_num
                                        else:
                                            raise Exception('---> El número debe contener solo dígitos.')
                                    if opcion == 8:
                                        personal_id = input('\nIngrese el ID personal de la persona => ')
                                        if personal_id.isdigit():
                                            data[0]['Telefonos'][2]['personal']['id'] = personal_id
                                        else:
                                            raise Exception('---> El ID debe contener solo dígitos.')
                                    if opcion == 9:
                                        personal_num = input('Ingrese el número personal de la persona => ')
                                        if personal_num.isdigit():
                                            data[0]['Telefonos'][2]['personal']['num'] = personal_num
                                        else:
                                            raise Exception('---> El número debe contener solo dígitos.')
                                    if opcion == 10:
                                        oficina_id = input('\nIngrese el ID de la oficina de la persona => ')
                                        if oficina_id.isdigit():
                                            data[0]['Telefonos'][3]['oficina']['id'] = oficina_id
                                        else:
                                            raise Exception('---> El ID debe contener solo dígitos.')
                                    if opcion == 11:
                                        oficina_num = input('Ingrese el número de la oficina de la persona => ')
                                        if oficina_num.isdigit():
                                            data[0]['Telefonos'][3]['oficina']['num'] = oficina_num
                                        else:
                                            raise Exception('---> El número debe contener solo dígitos.')
                                        
                                    peticion = requests.put(f"http://154.38.171.54:5502/personas/{id}", data=json.dumps(data[0]).encode("UTF-8"))
                                    res = peticion.json()
                                    res['Mensaje'] = '\nEl dato fue editado satisfactoriamente'
                                    print()
                                    print(res['Mensaje'])
                                    return [res]
                                
                                        
                                else:
                                    raise Exception ('\nPor favor, seleccione una opción válida de 1 a 11')
                            
                        elif opcion == 2:
                            break
                            
                    else:
                        raise Exception ('\nPor favor, seleccione una opción válida (1 o 2)')
                            
            except Exception as error:
                print('\n---ERROR---')
                print(error)
                break


def menuPersonal():
    while True:
        os.system('clear')
        print('''
                            
                        --- MENÚ PERSONAL ---
                            

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
                        print(tabulate(postPersonal(), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresione Enter para continuar...')
                    elif opcion == 2:
                        idedit = input('\nIngrese el ID asignado a la persona que la cual deseas editar un dato en SISTEMA G&C DE INVENTARIO CAMPUSLANDS => ')
                        print(tabulate(editPersonal(idedit), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresione Enter para continuar...')
                    elif opcion == 3:
                        while True:
                            os.system('clear')
                            print("""
                            A continuación eliminaras un personal existente de SISTEMA G&C DE INVENTARIO CAMPUSLANDS
                            
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
                                            iddelete = input('\nIngrese el ID de la persona que desea eliminar => ')
                                            deletePersonal(iddelete)
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
                    elif opcion == 4:
                        idsearch = input('\nIngresa el ID de la persona que deseas buscar de SISTEMA G&C DE INVENTARIO CAMPUSLANDS => ')
                        print()
                        print(tabulate(PersonasID(idsearch), headers='keys', tablefmt='fancy_grid'))
                        input('\nPresione Enter para continuar...')
                    elif opcion == 5:
                        break

        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')