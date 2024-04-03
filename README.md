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





- ### Documentación - Sistema G&C de Inventario CampusLands

  ¡Bienvenido al Sistema G&C de Inventario CampusLands! Este manual te guiará a través de las diferentes funciones disponibles en el sistema. A continuación, encontrarás una descripción de cada módulo y cómo puedes interactuar con ellos.

  ![image-20240401130814885](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401130814885.png)

  

  ---

  ## 1. Módulo de Activos 💻

  Este módulo te permite gestionar los activos registrados en el sistema por medio de esta url http://154.38.171.54:5501/activos donde podrás acceder a la base de datos del Sistema G&C de Inventario CampusLands . Puedes agregar nuevos activos, editar la información de los existentes, eliminar activos y buscar información específica de un activo.

  ![image-20240401130926951](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401130926951.png)

  #### Requisitos Previos:

  Antes de utilizar este módulo, asegúrate de tener instaladas las siguientes dependencias:

  - `requests`
  - `tabulate`
  
  Puedes instalarlas usando el siguiente comando en la terminal :
  
  `pip install requests tabulate`
  
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
  
  Se te pedirá una confirmación para poder proceder a editar un dato del activo seleccionado. Después de ingresar el "id" del activo a eliminar se mostrará un mensaje confirmando que se eliminó el activo en el Sistema G&C de Inventario CampusLands.
  
  ![image-20240401142651169](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401142651169.png)
  
  Ten en cuenta que si el activo está asignado a una persona o zona, no se podrá eliminar.
  
  ![image-20240401143123428](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401143123428.png)
  
  #### 4. Buscar Información de un Activo
  
  Si deseas buscar información detallada de un activo, selecciona la opción "Buscar" e ingresa el ID del activo que deseas encontrar. Se mostrará la información del activo correspondiente en el Sistema G&C de Inventario CampusLands.
  
  ![image-20240401143610367](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240401143610367.png)
  
  #### 5. Regresar al Menú Principal
  
  Al seleccionar, puedes regresar al menú principal seleccionando esta opción.
  
  ---
  
  ## 2. Módulo de Personal 👨‍💼
  
  Este módulo te permite gestionar el personal registrado en el sistema por medio de esta url http://154.38.171.54:5501/personas donde podrás acceder a la base de datos del Sistema G&C de Inventario CampusLands . Puedes agregar nuevos empleados, editar la información de los existentes, eliminar empleados y buscar información específica de un empleado.
  
  ![image-20240402074416652](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402074416652.png)
  
  **Interfaz del Usuario:**
  
  Al seleccionar la opción "Personal" en el menú principal, se mostrará un menú con las siguientes opciones
  
  #### 1. Agregar una Persona
  
  Para agregar una nueva persona al sistema, sigue estos pasos:
  
  Selecciona la opción "Agregar" en el menú de personal.
  
  ![image-20240402074334354](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402074334354.png)
  
  Se te solicitará confirmar si deseas continuar.
  
  ![image-20240402074531488](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402074531488.png)
  
  1. Ingresa la cédula de ciudadanía o el NIT de la persona. Este debe ser un número.
  
  2. Ingresa el nombre de la persona. Solo se permiten letras, espacios y guiones.
  
  3. Ingresa el correo electrónico de la persona. Debe seguir el formato estándar de un correo electrónico.
  
  4. Ingresa los números de teléfono asociados a la persona, como móvil, casa, personal y oficina. Debes ingresar el ID y el número de cada tipo de teléfono. Ambos deben ser números.
  
     ![image-20240402081755849](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402081755849.png)
  
  Después, se mostrará un mensaje confirmando que se agregó la persona en el Sistema G&C de Inventario CampusLands.
  
  #### 2. Editar una persona
  
  Permite editar la información de un empleado existente en el sistema.
  
  1. Selecciona la opción "Editar" en el menú de personal.
  
     ![image-20240402102451129](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402102451129.png)
  
  2. Ingresa el ID asignado a la persona que deseas editar.
  
     ![image-20240402103431495](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402103431495.png)
  
     Se te solicitará confirmar si deseas continuar.
  
     ![image-20240402103547198](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402103547198.png)
  
  3. Selecciona el dato que deseas actualizar:
  
     - Número de ID (CC, Nit)
     - Nombre
     - Email
     - ID y número de teléfono móvil
     - ID y número de teléfono de casa
     - ID y número de teléfono personal
     - ID y número de teléfono de oficina
  
     ![image-20240402104152567](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402104152567.png)
  
  4. Ingresa el nuevo valor para el dato seleccionado.
  
     ![image-20240402104245483](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402104245483.png)
  
     Al editar el dato correctamente, aparecerá una tabla donde puedes observar el dato editado que ingresaste junto con sus encabezados para actualizar al inventario Sistema G&C de Inventario CampusLands.
  
     ![image-20240402104821255](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402104821255.png)
  
     
  
  #### 3. Eliminar
  
  Para eliminar a una persona del sistema, sigue estos pasos:
  
  1. Selecciona la opción "Eliminar" en el menú de personal.
  
     ![image-20240402105335191](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402105335191.png)
  
  2. Se te solicitará confirmar si deseas continuar.
  
     ![image-20240402105419374](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402105419374.png)
  
  3. Ingresa el ID de la persona que deseas eliminar.
  
     ![image-20240402110604581](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402110604581.png)
  
  4. La persona será eliminada del sistema, a menos que tenga activos asignados, en cuyo caso se mostrará un mensaje indicando que no se puede eliminar.
  
     ![image-20240402110717251](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402110717251.png)
  
  #### 4. Buscar
  
  Para buscar información sobre una persona en el sistema, sigue estos pasos:
  
  1. Selecciona la opción "Buscar" en el menú de personal.
  
     ![image-20240402111643921](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402111643921.png)
  
  2. Ingresa el ID de la persona que deseas buscar.
  
     ![image-20240402111702015](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402111702015.png)
  
  3. Se mostrará la información de la persona encontrada, incluyendo su cédula o NIT, nombre, correo electrónico y números de teléfono asociados.
  
     ![image-20240402111444916](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402111444916.png)
  

####       5. Regresar al Menú Principal

​        Al seleccionar, puedes regresar al menú principal seleccionando esta opción.



---

## 3. Módulo de Zonas 🏢

Este módulo te permite gestionar las zonas registradas en el sistemapor medio de esta url http://154.38.171.54:5501/zonas donde podrás acceder a la base de datos del Sistema G&C de Inventario CampusLands . Puedes agregar nuevas zonas, editar la información de las existentes, eliminar zonas y buscar información específica de una zona.

![image-20240402191105711](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402191105711.png)

**Interfaz del Usuario:**

Al seleccionar la opción "Zonas" en el menú principal, se mostrará un menú con las siguientes opciones:

#### 1. Agregar

Esta opción te permite agregar una nueva zona al sistema. Para agregar una zona, sigue estos pasos:

1. Selecciona la opción "Agregar" en el menú de Zonas.

   ![image-20240402142401476](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402142401476.png)

   

2. Se te solicitará confirmar si deseas continuar.

   ![image-20240402142656441](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402142656441.png)

3. Ingresa el nombre de la zona en Campuslands. El nombre debe comenzar con mayúscula y seguir con letras minúsculas.

4. Ingresa la capacidad máxima de la zona en Campuslands. Este valor debe ser un número entero que represente la capacidad máxima de la zona.

   ![image-20240402142819711](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402142819711.png)

5. Después de ingresar los datos correctamente, aparecerá una tabla donde puedes observar los datos que ingresaste junto con sus encabezados para agregarlos al inventario Sistema G&C de Inventario CampusLands.

   ![image-20240402142940162](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402142940162.png)

   

#### 2. Editar

Con esta opción, puedes editar la información de una zona existente en el sistema. Sigue estos pasos para editar una zona:

1. Selecciona la opción "Editar" en el menú de Zonas.

   ![image-20240402143223009](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402143223009.png)

2. Ingresa el ID de la zona que deseas editar.

   ![image-20240402143301324](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402143301324.png)

   Se te solicitará confirmar si deseas continuar.

   ![image-20240402143417573](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402143417573.png)

3. Selecciona qué dato deseas actualizar: nombre de la zona o capacidad máxima.

   ![image-20240402143500355](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402143500355.png)

4. Ingresa el nuevo valor para el dato seleccionado.

   ![image-20240402143739909](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402143739909.png)

5. Al editar el dato correctamente, aparecerá una tabla donde puedes observar el dato editado que ingresaste junto con sus encabezados para actualizar al inventario Sistema G&C de Inventario CampusLands.

   ![image-20240402143822212](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402143822212.png)

   

#### 3. Eliminar

Puedes eliminar una zona del sistema con esta opción. Sin embargo, ten en cuenta que no podrás eliminar una zona si tiene activos asignados. Sigue estos pasos para eliminar una zona:

1. Selecciona la opción "Eliminar" en el menú de Zonas.

   ![image-20240402143958613](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402143958613.png)

   Se te pedirá una confirmación para poder continuar

   ![image-20240402144038530](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402144038530.png)

2. Ingresa el ID de la zona que deseas eliminar.

   ![image-20240402144102192](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402144102192.png)

3. La zona será eliminada del sistema, a menos que tenga activos asignados, en cuyo caso se mostrará un mensaje indicando que no se puede eliminar.

   ![image-20240402144844040](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402144844040.png)

   #### 4. Buscar

   Con esta opción, puedes buscar información específica sobre una zona utilizando su ID. Sigue estos pasos para buscar una zona:

   1. Selecciona la opción "Buscar" en el menú de Zonas.

      ![image-20240402190325065](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402190325065.png)

   2. Ingresa el ID de la zona que deseas buscar.

      ![image-20240402190301094](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402190301094.png)

   3. Se mostrará la información detallada de la zona encontrada.

      ![image-20240402190244531](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402190244531.png)

   #### 5. Regresar al Menú Principal

   ​    Al seleccionar, puedes regresar al menú principal seleccionando esta opción.

---

## 4. Módulo de Asignación de Activos 🧑‍💻

Este módulo te permite asignar activos a empleados o zonas por medio de esta url http://154.38.171.54:5501/activos donde podrás acceder a la base de datos y revisar cada activo con su respectiva asignación del Sistema G&C de Inventario CampusLands . Puedes asignar un activo a un empleado o a una zona específica, así como también puedes reasignar activos o liberarlos.

![image-20240402191238220](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402191238220.png)

**Interfaz del Usuario:**

Al seleccionar la opción "Asignación de activos" en el menú principal, se mostrará un menú con las siguientes opciones:

#### 1. Asignar

Esta opción te permite asignar un activo a un empleado o a una zona en el sistema. Sigue estos pasos para realizar una asignación:

1. Selecciona la opción "Crear asignación" en el menú principal del módulo de asignación de activos.

   ![image-20240402191437653](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402191437653.png)

   Se te pedirá una confirmación para continuar:

   ![image-20240402191535414](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402191535414.png)

2. Ingresa el ID del activo al cual deseas realizar la asignación. Asegúrate de ingresar un ID válido.

   ![image-20240402191619093](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402191619093.png)

3. Selecciona si la asignación será a una Zona o a una Persona.

   ![image-20240402191646279](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402191646279.png)

4. Ingresa el ID de la persona o zona a la cual deseas asignar el activo.

   ![image-20240402191711461](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402191711461.png)

5. ¡Listo! La asignación se realizará automáticamente y recibirás un mensaje de confirmación.

   ![image-20240402191733437](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402191733437.png)

#### 2. Buscar

Esta opción te permite buscar una asignación específica por su número de asignación. Sigue estos pasos para buscar una asignación:

1. Selecciona la opción "Buscar asignación" en el menú principal del módulo de asignación de activos.

   ![image-20240402192025377](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402192025377.png)

2. Ingresa el número de asignación del activo que deseas buscar.

   ![image-20240402192140762](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402192140762.png)

3. Se mostrará la información detallada de la asignación encontrada, incluyendo el activo asignado, la fecha de asignación y a quién se asignó.

   ![image-20240402192202807](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402192202807.png)

#### 3. Regresar

Al seleccionar, puedes regresar al menú principal seleccionando esta opción.



---

## 5. Módulo de Reportes ✉️

¡Bienvenido al módulo de reportes del Sistema G&C de Inventario CampusLands! 

![image-20240402192744992](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402192744992.png)

Aquí encontrarás diferentes opciones para visualizar información sobre los activos registrados y sus asignaciones.

#### Dependencias Requeridas

Para un correcto funcionamiento de este módulo, asegúrate de tener instaladas las siguientes dependencias:

- `requests`: Para realizar solicitudes HTTP a la API del sistema.
- `tabulate`: Para visualizar los datos en formato tabular.

**Interfaz del Usuario:**

Al seleccionar la opción "Reportes" en el menú principal, se mostrará un menú con las siguientes opciones:

![image-20240402192811879](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402192811879.png)

#### **1. Listar todos los activos**

- Esta opción te permite ver la lista completa de todos los activos registrados en el sistema.

  ![image-20240402192926397](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402192926397.png)

#### **2. Listar activos por categoría**

- Aquí puedes seleccionar una categoría específica para ver los activos asociados a esa categoría.

  ![image-20240402193226136](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402193226136.png)

  Al seleccionar la categoría procederá a darte los datos de los activos categorizados a la que elegiste:

  ![image-20240402193537260](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402193537260.png)

  Después de proveerte los datos de los activos te preguntara sí deseas observar otra categoría o deseas regresar al menú de Reportes

  ![image-20240402193718842](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402193718842.png)

#### **3. Listar activos dados de baja por daño**

- Muestra una lista de activos que han sido dados de baja debido a daños o problemas.

  ![image-20240402193851957](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402193851957.png)

#### **4. Listar activos y asignación**

- Te muestra una lista de activos junto con información sobre su asignación, si está asignado a alguien.

  ![image-20240402193938121](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402193938121.png)

#### **5. Listar historial de movimientos de activo**

- Aquí puedes ver un historial de movimientos de activos, como traslados entre zonas, cambios de estado, etc.

  ![image-20240402194007086](C:\Users\juand\AppData\Roaming\Typora\typora-user-images\image-20240402194007086.png)

#### 6. Regresar al menú principal

Al seleccionar, puedes regresar al menú principal seleccionando esta opción.





---

## 6. Módulo de Movimiento de Activos 🗒️

Este módulo te permite registrar los movimientos de los activos, como traslados entre zonas, cambios de estado, entre otros.

**Interfaz del Usuario:**

Al seleccionar la opción "Movimiento de activos" en el menú principal, se mostrará un menú con las siguientes opciones:

1. Registrar Movimiento: Permite registrar un nuevo movimiento de un activo.
2. Buscar Movimiento: Permite buscar información sobre un movimiento de activo por su ID.

---

#### 7. Salir

Esta opción te permite salir del sistema y finalizar la sesión.

---

¡Listo! Con esta guía podrás navegar por todas las funciones del Sistema G&C de Inventario CampusLands de manera fácil y rápida. Si tienes alguna duda, no dudes en consultar este manual. ¡Gracias por usar nuestro sistema!
