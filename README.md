# clase4tecfp
****** FUNDAMENTOS DE PROGRAMACIÓN ********

# Software de Gestión de Inventario para Ferretería

Este proyecto consiste en un software de gestión de inventario para una ferretería, desarrollado en Python con las librerías `pandas`, `tkinter` y `os`. Permite cargar datos de productos desde un archivo Excel, visualizar el inventario, calcular el IVA y generar informes sobre el estado del stock.

## Funcionalidades

* **Carga de datos:** Importa datos de productos desde un archivo Excel (`inventario_ferretería.xlsx`).
* **Visualización del inventario:** Muestra una tabla con los datos de los productos, incluyendo ID, nombre, cantidad, precio, fechas de compra y venta, IVA y observaciones sobre el stock.
* **Cálculo del IVA:** Calcula automáticamente el IVA (19%) para cada producto.
* **Informes de stock:** Indica si un producto está agotado o por debajo del stock mínimo.

## Requisitos

* Python 3.6 o superior
* Librería `pandas` (`pip install pandas`)
* Archivo Excel con los datos de los productos (`productos_ferreteria.xlsx`) en el mismo directorio que el script Python.

## Uso

1.  Clona el repositorio: `git clone https://github.com/amospinag/clase4tecfp.git`
2.  Navega al directorio del proyecto: `cd nombre_del_repositorio`
3.  Instala las dependencias: `pip install pandas`
4.  Instala las dependencias: `pip install tk`
5.  Instala las dependencias: `pip install os`
6.  Asegúrate de que los archivos `inventario_ferretería.xlsx` y `logo.png` estén en el mismo directorio que el script.
7.  Ejecuta el script: `python programa.py`

## Estructura del Proyecto

* `programa.py`: Script principal de Python que contiene la lógica del programa.
* `productos_ferreteria.xlsx`: Archivo Excel con los datos de los productos.

## Autores

* Andrés Mauricio Ospina Gonzalez
* Dauner Stiven Perdomo Bello
* Andrés Felipe Combariza Leguizamon
