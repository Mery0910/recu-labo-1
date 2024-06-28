import json

def menu_principal()-> str:
    """
    Esta funcion muestra el menu de opciones y guarda las respuesta.

    Return:
    (res) -> str
    """
    res = input("""
1 - Cargar archivo\n2 - Imprimir lista\n3 - Asignar totales
4 - Filtrar por tipo\n5 - Mostrar servicios\n6 - Guardar servicios\n7 - Salir\n
""")
    return res

def leer_json(ruta_archivo: str)-> list:
    """
    Esta funcion carga un archivo json y lo retorna.
    
    Parametros:
    (ruta_archivo) -> str

    Return:
    (data) -> list
    (False) -> bool
    """
    try:
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            return data
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo")
        return False
    except Exception as e:
        print(f"Error desconocido al cargar el archivo")
        return False
    
def mostrar_servicios(servicios)-> bool:
    """
    Esta funcion recorre una lista y muestra cada dato de cada servicio.

    Parametros:
    (servicios) -> list

    Return:
    (False) -> bool
    """
    if not servicios:
        print("La lista está vacía")
        return False

    else:
        print("{:<10}| {:<40} | {:<10} | {:<15} | {:<8} | {:<15}".format("id servicio","descripcion","tipo","precio Unitario","cantidad","total Servicio"))
        for servicio in servicios:
            print("{:<10} | {:<40} | {:<10} | {:<15} | {:<8} | {:<15} ".format(servicio["id_servicio"],servicio["descripcion"],servicio["tipo"],servicio["precioUnitario"],servicio["cantidad"],servicio["totalServicio"]))

def guardar_json(servicios:list, ruta_archivo:str):
    """
    Esta funcion guarda los datos proporcionados en un archivo JSON en la ruta obtenida.

    Parametros:
    (servicios) -> list
    (ruta_archivo) -> str
    """
    try:
        with open(ruta_archivo, 'w') as archivo:
            json.dump(servicios, archivo, indent=4)
    except Exception as e:
        print(f"Error desconocido al guardar el archivo")

def filtrar_por_tipo(servicios:list, tipo_seleccionado:str)-> list:
    """
    Esta funcion filtra los servicios por tipo y crea una lista filtrada y la retorna

    Parametros:
    (servicios) -> list
    (tipo_seleccionado) -> str

    Return:
    (servicios_filtrados) -> list
    """
    servicios_filtrados = []
    for servicio in servicios:
        if servicio["tipo"] == tipo_seleccionado:
            servicios_filtrados.append(servicio)

    return servicios_filtrados

def asignar_totales(servicios: list, key_1: str, key_2: str) -> list:
    """
    Esta funcion calcula el precio total de los productos y los asigna a la lista y la retorna.

    Parametros:
    (servicios) -> list
    (key_1) -> str
    (key_2) -> str

    Return:
    (servicios) -> list
    """
    precio_total = lambda s: float(s[key_1]) * float(s[key_2])
    for servicio in servicios:
        total = "{:.2f}".format(precio_total(servicio))
        servicio["totalServicio"] = str(total)
    return servicios

def ordenar_por_clave(lista:list,clave:str) -> list:
    """
    Esta funcion ordena la lista de manera ascendente por la clave asignada.

    Parametros:
    (lista) -> list
    (clave) -> str

    Returns:
    (lista) -> list
    """
    return sorted(lista, key=lambda servicio: servicio[clave])

def guardar_json(servicios: list, name: str):
    """
    Esta funcion crea un archivo json (si no existe) y guarda los servicioss de la lista.

    Parametros: 
    (servicios) -> list
    (name) -> str
    """
    with open(f"{name}.json", "w") as archivo:
        json.dump(servicios, archivo, indent = 4, ensure_ascii = False)