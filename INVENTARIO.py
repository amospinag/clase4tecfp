import pandas as pd

def cargar_productos(archivo):
    try:
        df = pd.read_excel(archivo, index_col=False)  # Evita que pandas use la primera columna como índice
        df.columns = df.columns.str.strip()  # Elimina espacios extra en los nombres de columna
        columnas_existentes = set(df.columns)
        columnas_requeridas = {'ID', 'Nombre', 'Cantidad', 'Precio', 'Fecha de Compra', 'Fecha de Venta'}
        if not columnas_requeridas.issubset(columnas_existentes):
            print(f"Error: El archivo debe contener las columnas: ID, Nombre, Precio, Cantidad")
            print(f"Columnas encontradas en el archivo: {df.columns.tolist()}")
            return None
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def mostrar_productos(df):
    df['IVA'] = df['Precio'] * 0.19
    df['Observación'] = ''  # Inicializar la columna 'Observación'
    for index, row in df.iterrows():
        if row['Cantidad'] == 0:
            df.loc[index, 'Observación'] = "Producto agotado"
        elif row['Cantidad'] <= 10:
            df.loc[index, 'Observación'] = "Producto por debajo de stock mínimo"

    print("Lista de productos disponibles:")
    print(df[['ID', 'Nombre', 'Cantidad', 'Precio', 'Fecha de Compra', 'Fecha de Venta', 'IVA', 'Observación']].to_string(index=False))  # Oculta el índice

def calcular_total(df):
    total = 0
    seleccionados = []
    while True:
        try:
            id_producto = input("Ingrese el ID del producto (o 'fin' para terminar): ")
            if id_producto.lower() == 'fin':
                break
            id_producto = int(id_producto)
            producto = df[df['ID'] == id_producto]
            if producto.empty:
                print("Producto no encontrado. Inténtelo de nuevo.")
                continue
            stock_disponible = producto.iloc[0]['Cantidad']
            if stock_disponible == 0:
                print(f"El producto {producto.iloc[0]['Nombre']} no lo tenemos disponible en este momento.")
                continue
            cantidad = int(input(f"Ingrese la cantidad de {producto.iloc[0]['Nombre']}: "))
            if cantidad > stock_disponible:
                print(f"Disculpe las molestias pero solo contamos con {stock_disponible} disponibles.")
                continue
            costo = cantidad * producto.iloc[0]['Precio']
            iva = costo * 0.19
            total += costo + iva
            seleccionados.append((producto.iloc[0]['Nombre'], cantidad, costo, iva))
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
    return seleccionados, total

def main():
    archivo = "inventario_ferretería.xlsx"
    df = cargar_productos(archivo)
    if df is None:
        return
    mostrar_productos(df)
    seleccionados, total = calcular_total(df)
    print("\nProductos seleccionados:")
    print("{:<15} {:<10} {:<10} {:<10}".format("Producto", "Cantidad", "Precio", "IVA")) # Encabezados de la tabla
    print("-" * 45) # Separador

    for producto in seleccionados:
        nombre, cantidad, precio, iva = producto
        print("{:<15} {:<10} {:<10.2f} {:<10.2f}".format(nombre[:15], cantidad, precio, iva)) # Datos de la tabla
    print("-" * 45) # Separador
    print(f"\nTotal: ${total:.2f}")
    print("-" * 45) # Separador

if __name__ == "__main__":
    main()

