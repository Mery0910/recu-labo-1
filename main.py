from funcionesrecu import *

opciones_habilitadas = False
punto5 = False
while True:
    opcion = menu_principal()
    print("")
    if opcion == "1":
            nombre_archivo = input("Ingrese la ruta del archivo JSON: ")
            lista = leer_json(nombre_archivo)
            if lista:
                opciones_habilitadas = True
                print("Lista obtenida")

    elif opciones_habilitadas == False and opcion != "7":
            print("Debe cargar un archivo para acceder al menú. Ingrese '1'")

    elif opcion == "2":
        mostrar_servicios(lista)

    elif opcion == "3":
        asignar_totales(lista,"cantidad","precioUnitario")
        mostrar_servicios(lista)

    elif opcion == "4":
        tipo_seleccionado = input("Ingrese el tipo que quiere filtrar (Hardware-Software): ")
        while tipo_seleccionado != "Hardware" and tipo_seleccionado != "Software":
            tipo_seleccionado = input("Reingrese el tipo que quiere filtrar (Hardware-Software): ")
            
        servicios_filtrados = filtrar_por_tipo(lista, tipo_seleccionado)
        guardar_json(servicios_filtrados, "lista_filtrada")

    elif opcion == "5":
        lista = ordenar_por_clave(lista,"descripcion")
        mostrar_servicios(lista)
        punto5 = True

    elif opcion == "6":
        if not punto5:
            print("Primero debe ejecutar la opcion 5 para guardar la lista")
        else:
             guardar_json(lista,"lista ordenada")
    elif opcion == "7":
        print("Saliendo del programa")
        break
    else:
        print("Ingrese una opción válida")