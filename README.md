# clase4tecfp
****** INTRODUCCIÓN A LA PROGRAMACIÓN********

# Software de Gestión de Inventario para Ferretería

Este proyecto consiste en un software de gestión de inventario para una ferretería, desarrollado en Python con la librería `pandas`. Permite cargar datos de productos desde un archivo Excel, visualizar el inventario, calcular el IVA y generar informes sobre el estado del stock.

## Funcionalidades

* **Carga de datos:** Importa datos de productos desde un archivo Excel (`productos_ferreteria.xlsx`).
* **Visualización del inventario:** Muestra una tabla con los datos de los productos, incluyendo ID, nombre, cantidad, precio, fechas de compra y venta, IVA y observaciones sobre el stock.
* **Cálculo del IVA:** Calcula automáticamente el IVA (19%) para cada producto.
* **Informes de stock:** Indica si un producto está agotado o por debajo del stock mínimo.
* **Cálculo de total de compra:** Permite seleccionar productos por ID y cantidad para calcular el total de una compra, incluyendo el IVA.
* **Impresión de tabla de productos seleccionados:** Muestra los productos seleccionados para la compra en formato de tabla, incluyendo nombre, cantidad, precio e IVA.

## Requisitos

* Python 3.6 o superior
* Librería `pandas` (`pip install pandas`)
* Archivo Excel con los datos de los productos (`productos_ferreteria.xlsx`) en el mismo directorio que el script Python.

## Uso

1.  Clona el repositorio: `git clone URL_DEL_REPOSITORIO`
2.  Navega al directorio del proyecto: `cd nombre_del_repositorio`
3.  Instala las dependencias: `pip install pandas`
4.  Asegúrate de que el archivo `productos_ferreteria.xlsx` esté en el mismo directorio que el script.
5.  Ejecuta el script: `python INVENTARIO.py`

## Estructura del Proyecto

* `INVENTARIO.py`: Script principal de Python que contiene la lógica del programa.
* `productos_ferreteria.xlsx`: Archivo Excel con los datos de los productos.

## Próximas Mejoras

* Implementación de una interfaz web con Flask o Django.
* Conexión a una base de datos para persistencia de datos.
* Funcionalidades adicionales de gestión de inventario (agregar, editar, eliminar productos).
* Despliegue en un servidor web o en la nube.

## Autores

* Andrés Mauricio Ospina Gonzalez
* Dauner Stiven Perdomo Bello
* Andrés Felipe Combariza Leguizamon
