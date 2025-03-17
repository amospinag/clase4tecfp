import pandas as pd
import tkinter as tk
from tkinter import ttk

# Cargar el archivo Excel
try:
    df = pd.read_excel("inventario_ferretería.xlsx")  # Busca el Excel llamado inventario_ferretería.xlsx
except FileNotFoundError:
    print("Error: No se encontró el archivo 'inventario.xlsx'. Asegúrate de que el archivo existe y está en el mismo directorio que el script.")
    exit()

# Función para calcular el IVA
def calcular_iva(precio):
    iva = precio * 0.19
    return iva

# Función para verificar el stock
def verificar_stock(cantidad, nombre_producto):
    msstock = ''
    if cantidad <= 10:
        if cantidad == 0:
            msstock = (f"El producto '{nombre_producto}' se ha agotado.")
        else:
            msstock = (f"Advertencia: El producto '{nombre_producto}' está por debajo de 10 unidades (Cantidad: {cantidad}).")
    return msstock

# Crear la interfaz gráfica
def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Inventario de Ferretería")

    # Crear un Treeview para mostrar los productos
    tree = ttk.Treeview(ventana, columns=("ID", "Nombre", "Cantidad", "Precio", "IVA", 'Mensajes'), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("Precio", text="Precio")
    tree.heading("IVA", text="IVA")

    # Insertar los productos en el Treeview
    for index, row in df.iterrows():
        tree.insert("", tk.END, values=(row["ID"], row["Nombre"], row["Cantidad"], row["Precio"], "",""))

    # Función para seleccionar productos y calcular el IVA
    def seleccionar_productos():
        productos_seleccionados = []
        for item in tree.selection():
            values = tree.item(item, "values")
            id_producto = values[0]
            nombre_producto = values[1]
            cantidad_producto = int(values[2])
            precio_producto = float(values[3])

            iva_producto = calcular_iva(precio_producto)
            tree.set(item, "IVA", f"${iva_producto:.2f}")  # Actualizar el IVA en el Treeview
            ms_stock = verificar_stock(cantidad_producto, nombre_producto)
            tree.set(item,"Mensajes", ms_stock)


            productos_seleccionados.append({
                "ID": id_producto,
                "Nombre": nombre_producto,
                "Cantidad": cantidad_producto,
                "Precio": precio_producto,
                "IVA": iva_producto,
                "Mesajes": ms_stock
            })

            verificar_stock(cantidad_producto, nombre_producto)  # Verificar el stock

        # Imprimir los productos seleccionados (opcional)
        print("\nProductos seleccionados:")
        for producto in productos_seleccionados:
            print(producto)

    # Botón para seleccionar productos
    boton_seleccionar = tk.Button(ventana, text="Seleccionar Productos", command=seleccionar_productos)

    tree.pack(pady=10)
    boton_seleccionar.pack(pady=10)

    ventana.mainloop()

# Crear la interfaz
crear_interfaz()