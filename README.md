# Proyecto-Python

DOCUMENTACIÓN MODULO PRINCIPAL

![image](https://github.com/Juannnrv/proyectoPython/assets/160557063/af1b679a-f1bd-4bfa-975d-9723eb31322b)


Descripción:

Este módulo define el punto de entrada principal del SISTEMA G&C DE INVENTARIO CAMPUSLANDS.

Funcionalidad:

El módulo muestra un menú con 7 opciones:
Activos: Permite gestionar los activos del sistema.
Personal: Permite gestionar el personal del sistema.
Zonas: Permite gestionar las zonas del sistema.
Asignación de activos: Permite asignar activos al personal.
Reportes: Permite generar reportes sobre el inventario del sistema.
Movimiento de activos: Permite registrar el movimiento de activos entre las diferentes zonas del sistema.
Salir: Permite salir del sistema.

Implementación:

El módulo utiliza un bucle while True para mostrar el menú y ejecutar la acción seleccionada por el usuario.
La función valida la entrada del usuario para asegurarse de que sea un número entero entre 1 y 7.
La función utiliza los módulos getActivos, getPersonal, getZonas, getAsignacionActivos, getReportes y getMovimientosActivos para mostrar los menús correspondientes a cada opción.

Documentación de los módulos:

getActivos: Contiene las funciones para gestionar los activos del sistema.
getPersonal: Contiene las funciones para gestionar el personal del sistema.
getZonas: Contiene las funciones para gestionar las zonas del sistema.
getAsignacionActivos: Contiene las funciones para gestionar la asignación de activos al personal.
getReportes: Contiene las funciones para generar reportes sobre el inventario del sistema.
getMovimientosActivos: Contiene las funciones para registrar el movimiento de activos entre las diferentes zonas del sistema.

Requisitos:

Los módulos getActivos, getPersonal, getZonas, getAsignacionActivos, getReportes y getMovimientosActivos deben estar en la misma carpeta que el módulo principal.

Errores:

Si el usuario ingresa una opción no válida, se mostrará un mensaje de error.
