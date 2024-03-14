# Prueba Técnica NumRot

## Requisitos previos

La prueba técnica se llevó a cabo en el lenguaje de programación Python, específicamente en su versión 3.12, por lo cual será necesario tener descargada esta versión en el dispositivo.

Durante la realización de la prueba se emplearon dependencias de terceros para alcanzar la solución, estas dependencias se encuentran registradas con su respectiva versión en el archivo requirements.txt, sin embargo, también se consignan a continuación:
- CTkMessagebox versión 2.5
- CTkSpinbox versión 1.3.0
- customtkinter versión 5.2.2
- darkdetect versión 0.8.0
- packaging versión 24.0
- pillow versión 10.2.0

## Manual para la ejecucion del proyecto realizado para la prueba técnica de la empresa NumRot.

### Contenido

El proyecto contiene dos carpetas principales: *primer_punto* e *interfaz_grafica_bd*.

En la carpeta *primer_punto* se encuentra el archivo *primer_punto.py*, el cual contiene la solución al primer punto propuesto en la prueba técnica.

En la carpeta *interfaz_grafica_bd* se encuentran las subcarpetas *bd, interfaz_grafica y usuario* que contienen las funcionalidades correspondientes a la base de datos, la interfaz gráfica del programa y el manejo de información del formulario respectivamente, necesarias para resolver los puntos 2, 3 y 4 de la prueba técnica. 

### Primer punto

Para visualizar la solución a este punto, se debe ejecutar el archivo *primer_punto.py* que se encuentra en la carpeta *primer_punto* en la terminal o a través de un IDE.

El aplicativo le pedirá inicialmente al usuario 3 variables: A, B y C, siguiendo la forma de ecuación cuadrática: A<sup>2</sup> + B<sup>2</sup> = C<sup>2</sup>, de las cuales se debe dejar una en blanco para calcular su solución.

Aunque el aplicativo se diseñó con la intención de dejar una variable en blanco, puede manejar los casos cuando las variables no son numéricas, cuando se deja más de una variable en blanco, cuando no se deja variable en blanco y cuando la solución no existe.

### Segundo punto

Para visualizar la solución a este punto, se debe ejecutar el archivo *main.py* que se encuentra en la carpeta raíz del proyecto en la terminal o a través de un IDE.

A continuación se abrirá una ventana que le pedirá indicar la ruta donde se guardará la base de datos (archivo .db), o en su defecto, indicar la base de datos con la cual se trabajará (archivo .db).

Luego se abrirá una ventana denominada *Formulario de datos* que tendrá una serie de campos en el costado derecho que deben ser diligenciados. Esta ventana también cuenta con 3 botones en el costado inferior que tienen las funcionalidades: limpiar los campos diligenciados, validar y enviar los datos diligenciados y analizar los registros almacenados en la base de datos.

### Tercer punto

Una vez diligenciados los datos en el formulario, se debe presionar el botón **Ingresar información**, el cual validará que los datos diligenciados en el formulario estén correctos y que no haya campos obligatorios sin diligenciar, luego, se conectará con la base de datos y guardará un registro de los datos diligenciados.

### Cuarto punto

Si la base de datos cuenta con menos de 10 registros, cuando se presione el botón **Analizar información** saltará un aviso informando que aún no cuenta con los registros necesarios. Una vez la base de datos cuente con los diez registros mínimos, presionar el botón **Analizar información** abrirá una nueva ventana que contiene 5 botones, los cuales tienen vinculadas funcionalidades de consulta a la base de datos, siendo estas:

- Consultar el nombre completo de todas las personas registradas
- Consultar el número de personas con el género *Mujer*
- Consultar el número de personas con el género *Hombre*
- Consultar el nombre completo de la persona registrada con mayor edad
- Consultar el promedio de edad de todas las personas registradas








