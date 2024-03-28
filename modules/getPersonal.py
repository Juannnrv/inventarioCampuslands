import re
import json
import os 
import requests
from tabulate import tabulate

def Personas():
    peticion = requests.get('http://154.38.171.54:5502/personas')
    data = peticion.json()
    return data

def PersonasID(id):
    for val in Personas():
        if val.get('id') == id:
            return [val]
        
def postPersonal():

    personas = {
    "id": "2",
    "nroId (CC, Nit)": "1003697855",
    "Nombre": "Orbin Pabon",
    "Email": "orbinpabon@example.com",
    "Telefonos": [
      {
        "movil": {
          "id": "2",
          "num": "3002014590"
        },
        "casa": {
          "id": "2",
          "num": "3002014591"
        }
      }
    ]
  }
    while True:
        os.system('clear')
        print("""
        A continuación agregaras una nueva persona a SISTEMA G&C DE INVENTARIO CAMPUSLANDS
        
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
                            # os.system('clear')
                            # try:
                            #     if 'id' not in personas:
                            #         idpersona = input('Ingrese el ID de la persona => ')
                            #         if idpersona.isdigit():
                            #             idpersona = int(idpersona)
                            #             if idpersona > 0:
                            #                 data = PersonasID(idpersona)
                            #                 if data:
                            #                     raise Exception('El ID de la persona ya existe')
                            #                 else:
                            #                     personas['id'] = idpersona
                            #                     break
                            #             else:
                            #                 raise Exception('---> El ID de la persona debe ser un número positivo')
                            #         else:
                            #             raise Exception('---> El ID de la persona no cumple con el estándar establecido')
                            # except Exception as error:
                            #     print(error)

                                if 'nroId (CC, Nit)' not in personas:
                                    nroId = input('\nIngrese la Cc o Nit de la persona => ')
                                    if nroId.isdigit():
                                        nroId = int(nroId)
                                        personas['nroId (CC, Nit)'] = nroId
                                    else:
                                        raise Exception('---> La Cc o Nit de la persona no cumple, debes ingresar números')
                                    
                                if 'Nombre' not in personas:
                                    nombre = input('\nIngrese el nombre de la persona => ')
                                    if re.match(r'^[a-zA-Z0-9\s-]+$', nombre):
                                        personas['Nombre'] = nombre
                                    else:
                                        raise Exception('---> El nombre de la persona no cumple, debes ingresar letras')
                                    
                                if 'Email' not in personas:
                                    email = input('\nIngrese el email de la persona => ')
                                    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$', email):
                                        personas['Email'] = email
                                    else:
                                        raise Exception('---> El email de la persona no cumple con el estandar establecido')
                                                                            
                                if 'Telefonos' not in personas:
                                    personas['Telefonos'] = []  # Si la lista de teléfonos no existe, créala

                                    #MOVIL
                                    # Solicitar al usuario el ID y el número de teléfono móvil
                                    movil_id = input('\nIngrese el ID del móvil de la persona => ')
                                    movil_num = input('\nIngrese el número de móvil de la persona => ')

                                    # Verificar que el ID y el número de teléfono móvil sean dígitos
                                    if movil_id.isdigit() and movil_num.isdigit():
                                        movil_id = int(movil_id)
                                        movil_num = int(movil_num)

                                        # Agregar el número de teléfono móvil a la lista 'Telefonos' con la estructura correcta
                                        personas['Telefonos'].append({"movil": {"id": movil_id, "num": movil_num}})
                                    else:
                                        raise Exception('---> El ID y el número de móvil deben contener solo dígitos.')
                                    
                                    # CASA
                                    casa_id = input('\nIngrese el ID del número asignado a la casa de la persona => ')
                                    casa_num = input('\nIngrese el número de la casa de la persona => ')
                                    if casa_id.isdigit() and casa_num.isdigit():
                                        casa_id = int(casa_id)
                                        casa_num = int(casa_num)
                                        personas['Telefonos'].append({"casa": {"id": casa_id, "num": casa_num}})
                                    else:
                                        raise Exception('---> El ID y el número de móvil deben contener solo dígitos.')
                                    
                                    #PERSONAL
                                    personal_id = input('\nIngresa el ID del número personal => ')
                                    personal_num = input('\nIngrese el número personal => ')
                                    if personal_id.isdigit() and personal_num.isdigit():
                                        personal_id = int(personal_id)
                                        personal_num = int(personal_num)
                                        personas['Telefonos'].append({"personal": {"id": personal_id, "num": personal_num}})
                                    else:
                                        raise Exception('---> El ID y el número de móvil deben contener solo dígitos.')
                                    
                                    #OFICINA
                                    oficina_id = input('\nIngrese el ID asignado a la oficina de la persona => ')
                                    oficina_num = input('\nIngrese el número asignado a la oficina de la persona => ')
                                    if oficina_id.isdigit() and oficina_num.isdigit():
                                        oficina_id = int(oficina_id)
                                        oficina_num = int(oficina_num)
                                        personas['Telefonos'].append({"oficina": {"id": oficina_id, "num": oficina_num}})
                                    else:
                                        raise Exception('---> El ID y el número de móvil deben contener solo dígitos.')
                                    
                                    break

                                else:
                                    raise Exception('---> El dato ya existe')
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

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5502/personas', headers=headers, data=json.dumps(personas, indent=4))
    res = peticion.json()
    res ['Mensaje'] = '\Persona guardada satisfactoriamente'
    print(res['Mensaje'])
    input('\nPresione Enter para continuar...')
    return [res]


# def deletePersonal():


# def editPersonal():


# def searchAsignacionActivos():
        #Para obtener un activo específico por su ID: GET /activos/{id}



def menuPersonal():
    while True:
        os.system('clear')
        print('''
                            ---MENÚ PERSONAL---

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
                        postPersonal()
                    # elif opcion == 2:
                    #     deletePersonal()
                    # elif opcion == 3:
                    #     editPersonal()
                    # elif opcion == 4:
                    #     searchPersonal()
                    # elif opcion == 5:
                    #     break

        except KeyboardInterrupt:
            print('\nRegresando al menú principal...')