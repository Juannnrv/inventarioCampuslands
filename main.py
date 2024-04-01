import os
import re
import modules.getActivos as gA
import modules.getPersonal as gP
import modules.getZonas as gZ
import modules.getAsignacionActivos as gAsig
import modules.getReportes as gR
import modules.getMovimientosActivos as gMovA



if __name__ == "__main__":
    while True:
        os.system('clear')
        print('''
                    
                        --- SISTEMA G&C DE INVENTARIO CAMPUSLANDS --- 
                    
                    
                                1. 💻 Activos
                                
                                2. 👨‍💼 Personal
                                
                                3. 🏢 Zonas
                                
                                4. 🧑‍💻 Asignación de activos
                                
                                5. ✉️  Reportes
                                
                                6. 🗒️  Movimiento de activos
                                
                                
                                7. Salir
''')
        opcion = input('\nSeleccione una de las opciones => ')
        if re.match(r'[0-9]+$', opcion):
            opcion = int(opcion)
            if opcion >= 0 and opcion <= 7:
                if opcion == 1:
                    gA.menuActivos()
                elif opcion == 2:
                    gP.menuPersonal()
                elif opcion == 3:
                    gZ.menuZonas()
                elif opcion == 4:
                    gAsig.menuAsignacionActivos()
                elif opcion == 5:
                    gR.menuReportes()
                elif opcion == 6:
                    gMovA.menuMovimientoActivos()
                elif opcion == 7:
                    break

                
                
                
    
    