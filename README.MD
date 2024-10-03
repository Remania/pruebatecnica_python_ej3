# Proyecto Algoritmo en Python

Este repositorio contiene una algoritmo desarrollado con el lenguaje Python. A continuación, se explican los pasos para clonar y ejecutar este proyecto localmente.

## Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener instalado lo siguiente en tu máquina:

- Python (versión 3.8 o superior)
- pip (gestor de paquetes de Python)
- Git

## Instrucciones para clonar y ejecutar el proyecto

### 1. Clonar el repositorio

Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

git clone https://github.com/Remania/pruebatecnica_python_ej3.git

### 2. Instala las dependencias

Instala las dependencias necesarias con el siguiente comando:

pip install -r requirements.txt

### 3. Ejecutar el script

Una vez configurado todo, ejecuta el script app.py con el siguiente comando:

python app.py

## Funcionamiento del Algoritmo de Lectura de Archivos .txt

El algoritmo diseñado para filtrar URLs válidas de un archivo .txt opera de la siguiente manera:

1. **Inicialización del Tiempo**: Se registra el tiempo de inicio para medir la duración de la ejecución del algoritmo.

2. **Definición de la Función `filtrar_urls`**: Esta función recibe como argumento el nombre del archivo que contiene las URLs.

3. **Lectura y Filtrado de URLs**: Utilizando una comprensión de conjuntos, se lee el archivo línea por línea. Para cada línea, se realizan las siguientes operaciones:
   - Se elimina cualquier espacio en blanco al inicio y al final de la línea.
   - Se verifica si la línea no está vacía, contiene la palabra "shop" y termina con ".html".
   - Si todas estas condiciones son verdaderas, la URL se agrega al conjunto `urls_validas`.

4. **Resultados**: Al finalizar la lectura, se cuenta el número total de URLs válidas y se imprime el resultado. Si no se encuentran URLs válidas, se imprime un mensaje adecuado.

5. **Cálculo del Tiempo de Ejecución**: Se registra el tiempo de finalización y se calcula el tiempo total que tomó ejecutar el algoritmo, mostrando este valor al usuario.

## Técnicas Utilizadas para Optimizar el Rendimiento y el Uso de Memoria

1. **Comprensión de Conjuntos**: El uso de una comprensión de conjuntos (`{...}`) permite construir el conjunto `urls_validas` en una sola línea, lo que simplifica el código y mejora la legibilidad. Además, esta técnica automáticamente evita duplicados, ya que los conjuntos solo almacenan elementos únicos.

2. **Lectura Eficiente del Archivo**: Al leer el archivo directamente dentro de la comprensión de conjuntos, se reduce el uso de memoria al no almacenar todo el contenido del archivo en una lista o variable temporal. Esto es especialmente útil para archivos grandes, ya que solo mantiene en memoria lo necesario para cada línea.

3. **Condiciones de Filtrado Directas**: Las condiciones de verificación (comprobación de vacío, inclusión de "shop" y verificación de extensión) se realizan en una sola línea, lo que optimiza el tiempo de procesamiento por línea y reduce la complejidad del código.

4. **Evitar Almacenamiento Redundante**: Al utilizar un conjunto para almacenar las URLs válidas, se elimina el almacenamiento innecesario de duplicados, lo que ahorra espacio en memoria y mejora el rendimiento general.

