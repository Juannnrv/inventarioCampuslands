# ---Proyecto-Python---

### "Sistema G&C de Inventario CampusLands"

#### Descripción

Este programa proporciona una interfaz de usuario para el sistema de gestión de inventario de CampusLands. Permite llevar un control detallado de los activos ubicados en la sede principal de Bucaramanga. Los activos pueden ser asignados a empleados, cambiar de ubicación, ser dados de baja por daño o enviados a mantenimiento. Además, el programa gestiona información sobre el personal que labora en la organización y las zonas dentro del campus.

#### Funcionalidades Principales

1. Gestión de Activos: Permite agregar, editar, eliminar y buscar activos, así como regresar al menú principal.
2. Gestión de Personal: Proporciona opciones para agregar, editar, eliminar y buscar personas, y volver al menú principal.
3. Gestión de Zonas: Ofrece funcionalidades para agregar, editar, eliminar y buscar zonas, además de regresar al menú principal.
4. Asignación de Activos: Permite crear y buscar asignaciones de activos, y volver al menú principal.
5. Reportes: Genera diferentes tipos de reportes sobre los activos, como listar todos los activos, listar por categoría, listar activos dados de baja por daño, listar activos con asignaciones y listar historial de movimientos de activos. También proporciona la opción de regresar al menú principal.
6. Movimiento de Activos: Ofrece opciones para el retorno de activos, dar de baja activos, cambiar asignaciones de activos y enviar activos a garantía, además de regresar al menú principal.
7. Salir: Permite salir del programa.

#### Condiciones Especiales

1. Restricciones en Asignación: No se puede asignar o reasignar un activo que se encuentre en reparación o garantía.
2. Restricción de Asignación: No se puede asignar un activo que esté dado de baja.
3. Estado del Activo: Para asignar un equipo, debe estar en estado "no asignado".
4. Restricción de Eliminación: No se puede eliminar personas que tengan activos asignados.
5. Restricción de Eliminación: No se puede eliminar un activo asignado a una persona o zona del campus.





- ### Manual de Usuario - Sistema G&C de Inventario CampusLands

  ¡Bienvenido al Sistema G&C de Inventario CampusLands! Este manual te guiará a través de las diferentes funciones disponibles en el sistema. A continuación, encontrarás una descripción de cada módulo y cómo puedes interactuar con ellos.

  ![image-20240401130814885](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401130814885.png)

  ---

  #### 1. Módulo de Activos 💻

  Este módulo te permite gestionar los activos registrados en el sistema por medio de esta url http://154.38.171.54:5501/activos donde podrás acceder a la base de datos del Sistema G&C de Inventario CampusLands . Puedes agregar nuevos activos, editar la información de los existentes, eliminar activos y buscar información específica de un activo.

  ![image-20240401130926951](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401130926951.png)

  **Interfaz del Usuario:**

  Al seleccionar la opción "Activos" en el menú principal, se mostrará un menú con las siguientes opciones:

  #### 1. Agregar un Nuevo Activo

  Al seleccionar la opción "Agregar", a continuación se te pedirá una confirmación para poder proceder a agregar el activo.

  ![image-20240401132959418](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401132959418.png)

  Al seleccionar la opción "1", podrás ingresar los datos del nuevo activo siguiendo las siguientes indicaciones y observando la imagen de referencia. Se te solicitará ingresar los siguientes datos:

  - **Número de Item:** Identificación única del activo (número entero).

  - **Código de Transacción:** Código numérico asociado a la transacción del activo.

  - **Número de Serial (Opcional):** Número de serie del activo (opcional).

    ![image-20240401133435893](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401133435893.png)

    Al seleccionar la opción "1", debes ingresar el número del serial único (combinación de letras mayúsculas y números enteros).

    Al seleccionar la opción "2", no se le asignara el número de serial  ("Sin serial")

  - **Código del Campus:** Identificador único del campus donde se encuentra el activo (3 letras en mayúscula seguidas de 3 números).

  - **Número de Formulario:** Identificación única del formulario del activo. (Números enteros)

  - **Nombre del Activo:** Nombre identificador del activo.

  - **Proveedor del Activo:** Nombre del proveedor del activo.

  - **Empresa Responsable:** Nombre de la empresa responsable del activo.

  - **Marca del Activo:** Selección de la marca del activo.

  - **Categoría del Activo:** Selección de la categoría del activo.

  - **Tipo de Activo:** Selección del tipo de activo.

  - **Valor Unitario del Activo:** Valor monetario unitario del activo.

    ![image-20240401135151961](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401135151961.png)

    Después de ingresar los datos correctamente, aparecerá una tabla donde puedes observar los datos que ingresaste junto con sus encabezados para agregarlos al inventario Sistema G&C de Inventario CampusLands.

    <img src="C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401135409287.png" alt="image-20240401135409287" style="zoom: 200%;" />

  #### 2. Editar un Activo Existente

  Puedes modificar un dato de un activo seleccionando la opción "Editar" e ingresando el ID del activo que deseas editar.

  ![image-20240401141250286](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401141250286.png)

  se te pedirá una confirmación para poder proceder a editar un dato del activo seleccionado.

  ![image-20240401140050138](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401140050138.png)

  Luego podrás elegir qué datos deseas actualizar, como el número de item, el nombre, el valor unitario, entre otros.

  ![image-20240401140118938](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401140118938.png)

  Podrás escoger que dato editar según el número asignado teniendo en cuenta las indicaciones dadas anteriormente en Agregar Activos donde puedes observar como debes ingresar cada dato.

  ![image-20240401135151961](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401135151961.png)

  Al editar el dato correctamente, aparecerá una tabla donde puedes observar el dato editado que ingresaste junto con sus encabezados para actualizar al inventario Sistema G&C de Inventario CampusLands.

  ![image-20240401141140055](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401141140055.png)

  #### 3. Eliminar un Activo

  Para eliminar un activo, selecciona la opción "Eliminar" e ingresa el ID del activo que deseas eliminar (solo cambiará su estado a "No asignado").

  ![image-20240401141518950](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401141518950.png)

  Se te pedirá una confirmación para poder proceder a editar un dato del activo seleccionado. Después de ingresar el "id" del activo a eliminar se mostrará un mensaje afirmando que se eliminó el activo en el Sistema G&C de Inventario CampusLands.

  ![image-20240401142651169](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401142651169.png)

  Ten en cuenta que si el activo está asignado a una persona o zona, no se podrá eliminar.

  ![image-20240401143123428](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401143123428.png)

  #### 4. Buscar Información de un Activo

  Si deseas buscar información detallada de un activo, selecciona la opción "Buscar" e ingresa el ID del activo que deseas encontrar. Se mostrará la información del activo correspondiente en el Sistema G&C de Inventario CampusLands.

  ![image-20240401143610367](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401143610367.png)

  #### 5. Regresar al Menú Principal

  En cualquier momento, puedes regresar al menú principal seleccionando esta opción.

  ¡Ahora estás listo para comenzar a gestionar los activos en el sistema! Si tienes alguna pregunta o necesitas ayuda, no dudes en consultar este manual.

  ---

  #### 2. Módulo de Personal 👨‍💼

  Este módulo te permite gestionar el personal registrado en el sistema. Puedes agregar nuevos empleados, editar la información de los existentes, eliminar empleados y buscar información específica de un empleado.

  **Interfaz del Usuario:**

  Al seleccionar la opción "Personal" en el menú principal, se mostrará un menú con las siguientes opciones:

  1. Agregar: Permite agregar un nuevo empleado al sistema.
  2. Editar: Permite editar la información de un empleado existente en el sistema.
  3. Eliminar: Permite eliminar un empleado del sistema.
  4. Buscar: Permite buscar información específica de un empleado por su ID.

  ![Interfaz de Personal](ruta/a/la/imagen/personal.png)

  ---

  #### 3. Módulo de Zonas 🏢

  Este módulo te permite gestionar las zonas registradas en el sistema. Puedes agregar nuevas zonas, editar la información de las existentes, eliminar zonas y buscar información específica de una zona.

  **Interfaz del Usuario:**

  Al seleccionar la opción "Zonas" en el menú principal, se mostrará un menú con las siguientes opciones:

  1. Agregar: Permite agregar una nueva zona al sistema.
  2. Editar: Permite editar la información de una zona existente en el sistema.
  3. Eliminar: Permite eliminar una zona del sistema.
  4. Buscar: Permite buscar información específica de una zona por su ID.

  ![Interfaz de Zonas](ruta/a/la/imagen/zonas.png)

  ---

  #### 4. Módulo de Asignación de Activos 🧑‍💻

  Este módulo te permite asignar activos a empleados o zonas. Puedes asignar un activo a un empleado o a una zona específica, así como también puedes reasignar activos o liberarlos.

  **Interfaz del Usuario:**

  Al seleccionar la opción "Asignación de activos" en el menú principal, se mostrará un menú con las siguientes opciones:

  1. Asignar: Permite asignar un activo a un empleado o a una zona.
  2. Reasignar: Permite reasignar un activo a otro empleado o a otra zona.
  3. Liberar: Permite liberar un activo asignado.
  4. Buscar: Permite buscar información sobre la asignación de activos por su ID.

  ![Interfaz de Asignación de Activos](ruta/a/la/imagen/asignacion_activos.png)

  ---

  #### 5. Módulo de Reportes ✉️

  Este módulo te permite generar diferentes tipos de reportes sobre los activos y la asignación de los mismos. Puedes generar reportes de inventario, reportes de asignaciones y más.

  **Interfaz del Usuario:**

  Al seleccionar la opción "Reportes" en el menú principal, se mostrará un menú con las siguientes opciones:

  1. Generar Reporte de Inventario: Permite generar un reporte con la lista de todos los activos registrados en el sistema.
  2. Generar Reporte de Asignaciones: Permite generar un reporte con la lista de asignaciones de activos.
  3. Generar Otros Reportes: Permite generar otros tipos de reportes específicos.

  ![Interfaz de Reportes](ruta/a/la/imagen/reportes.png)

  ---

  #### 6. Módulo de Movimiento de Activos 🗒️

  Este módulo te permite registrar los movimientos de los activos, como traslados entre zonas, cambios de estado, entre otros.

  **Interfaz del Usuario:**

  Al seleccionar la opción "Movimiento de activos" en el menú principal, se mostrará un menú con las siguientes opciones:

  1. Registrar Movimiento: Permite registrar un nuevo movimiento de un activo.
  2. Buscar Movimiento: Permite buscar información sobre un movimiento de activo por su ID.

  ![Interfaz de Movimiento de Activos](ruta/a/la/imagen/movimiento_activos.png)

  ---

  #### 7. Salir

  Esta opción te permite salir del sistema y finalizar la sesión.

  ---

  ¡Listo! Con esta guía podrás navegar por todas las funciones del Sistema G&C de Inventario CampusLands de manera fácil y rápida. Si tienes alguna duda, no dudes en consultar este manual. ¡Gracias por usar nuestro sistema!
