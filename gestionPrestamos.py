from validaciones import validarEntero
from datetime import  date, datetime, timedelta
from gestionHerramientas import ARCHIVO1, listarHerramienta, actualizarEstadoPorStock
from gestionUsuariosGeneral import ARCHIVO2, existeResidente
from gestionHerramientas import cargar, guardar, generar_id
from historialAcciones import log

ARCHIVO4= "prestamos.json"

#esto solo lo tiene el usuario o residente
def solicitarPrestamos(usuario_actual):
    prestamos=cargar(ARCHIVO4)
    herramientas=cargar(ARCHIVO1)
    usuarios=cargar(ARCHIVO2)
    usuario_actual=existeResidente("Ingrese su id de usuario")
    #se listan para que sepan cuales hay
    listarHerramienta()
    id_herramienta=validarEntero("Ingrese el ID de la herramienta que desea solicitar: ")
    for herramienta in herramientas:
        if herramienta["id"] == id_herramienta:
            if herramienta["estado"] == "disponible":
                guardar(ARCHIVO1, herramientas)
                cantidad_solicitada = validarEntero("Ingrese la cantidad de herramientas que desea solicitar: ")

                #en este pasito, se busca que la cantidad solicitada sea valida 
                while cantidad_solicitada == None or cantidad_solicitada <= 0 or cantidad_solicitada>stock_herramienta:
                    log("cantidad invalidada","El usuario ha puesto un número no disponible en el stock", date.today(), "residente")
                    cantidad_solicitada = validarEntero("Error, ingrese una cantidad válida: ")
                stock_herramienta = herramienta["stock"]

                #y no pase la cantidad que hay
                if stock_herramienta >= cantidad_solicitada:
                    # No se descuenta el stock aquí, se descontará cuando el admin apruebe el préstamo
                    print("Ingrese los datos y el administrador aceptará o rechazará prestar la herramienta")
                    pass
                else:
                    print("No hay suficiente stock disponible.")
                    log("cantidad invalidada","El usuario ha puesto un número no disponible en el stock", date.today(), "residente")
                    return
                
                #dias que necesita la herramienta
                dias_prestamo=int(input("Ingrese dias necesita la herramienta: "))
                fecha_final_prestamo=(datetime.now() + timedelta(days=dias_prestamo))
                #el precio del prestamo por dia
                precio_base = 2000
                observaciones=input("Ingrese alguna observacion sobre el prestamo:")

                #cada herramienta es distinta y sus precios de alquiler varian
                precio_alquiler = herramienta.get("precio de alquiler", 0)
                print(f"Precio del préstamo: ${precio_base} * {dias_prestamo} dias, + ${precio_alquiler} del alquiler de la herramienta  = ${precio_alquiler + (precio_base * dias_prestamo)}")
                
                #aqui se dice como se tomará el precio final
                usuario = validarEntero("Ingrese su ID de usuario para solicitar el préstamo: ")
                precio_prestamo = precio_base* dias_prestamo + herramienta.get("precio de alquiler", 0) 
                if not existeResidente(usuario):
                    log("usuario no existe","El usuario ha puesto un id no registrado", date.today(), "residente")
                    print("El id no existe en el sistema")
                    return
                
                #se genera un nuevo prestamo que el admin debe aceptar o rechazar y ademas el usuario lo puede ver en prestamos hechos
                nuevo_prestamo = {
                    "id": generar_id(prestamos),
                    "herramienta_id": id_herramienta,
                    "usuario": usuario,
                    "fecha_prestamo": str(date.today()),
                    "fecha_devolucion": str(fecha_final_prestamo),
                    "precio": precio_prestamo,
                    "observaciones": observaciones,
                    "estado": "pendiente"
                }
                #se guarda en json
                prestamos.append(nuevo_prestamo)
                guardar(ARCHIVO4, prestamos)

                print("¡Préstamo solicitado con éxito! Pendiente de aprobación por el administrador.")
                print("Consulte sus prestamos para ver si el prestamo fue aprobado por el administrador.")
                log("solicitar prestamo", "se solicitó un préstamo de herramienta", date.today(), "residente")
                break
            else:
                print("La herramienta no está disponible para préstamo.")
                return
        
#aqui es q el usuario puede ver sus prestamos activos, o sea los que el admin ya aprobó, pero no los pendientes ni los rechazados
def solicitudesPendientes():
    prestamos=cargar(ARCHIVO4)
    herramientas=cargar(ARCHIVO1)
    usuarios=cargar(ARCHIVO2)
    print("Mis Préstamos Activos:")
    for prestamo in prestamos:
        if prestamo["estado"] == "prestado":
            herramienta = next((herramienta for herramienta in herramientas if herramienta["id"] == prestamo["herramienta_id"]), None)
            usuario = next((u for u in usuarios if u["id"] == prestamo["usuario"]), None)
            if herramienta and usuario:
                print(f'ID Prestamo: {prestamo["id"]}\tHerramienta: {herramienta["nombre"]}\tUsuario: {usuario["nombre"]}\tFecha de Devolución: {prestamo["fecha_devolucion"]}\tObservaciones: {prestamo["observaciones"]}')
    print()


#esto lo tiene el admin, para que vea los prestamos pendientes
def aprobarRechazarPrestamos():
    #Función para que el administrador apruebe o rechace préstamos pendientes
    prestamos = cargar(ARCHIVO4)
    herramientas = cargar(ARCHIVO1)
    usuarios = cargar(ARCHIVO2)
    
    # Buscar préstamos pendientes
    prestamos_pendientes = [p for p in prestamos if p["estado"] == "pendiente"]
    
    if not prestamos_pendientes:
        log("Prestamos", "No hay prestamo pendiente por aprobar", date.today(), "Administrador")
        print("\nNo hay préstamos pendientes de aprobación.")
        return
    
    print("\n" + "="*60)
    print("PRÉSTAMOS PENDIENTES POR SU APROBACIÓN")
    print("="*60)
    
    for prestamo in prestamos_pendientes:
        #aquí se usa el next como si fuera un .get, solo que get es para diccionarios y next para listas
        #además, next() busca por una condicion, además retorna el primer elemento que cumpla esa condicion
        #en este codigo, mis usuarios osn listas de diccionarios, por lo que si no encuentra nada, tira None
        herramienta = next((h for h in herramientas if h["id"] == prestamo["herramienta_id"]), None)
        usuario = next((u for u in usuarios if u["id"] == prestamo["usuario"]), None)
        
        if herramienta and usuario:
            print(f"\nID Préstamo: {prestamo['id']}")
            print(f"  Herramienta: {herramienta['nombre']}")
            print(f"  Solicitante: {usuario['nombre']} {usuario['apellido']}")
            print(f"  Fecha Préstamo: {prestamo['fecha_prestamo']}")
            print(f"  Fecha Devolución: {prestamo['fecha_devolucion']}")
            print(f"  Precio: ${prestamo['precio']}")
            print(f"  Observaciones: {prestamo['observaciones']}")
    # si no quiere aporobar ninguno, pues darle la opcion de salir de ahí
    print("\n" + "="*60)
    id_prestamo = validarEntero("Ingrese el ID del préstamo que desea gestionar (0 para SALIR sin aprobar): ")
    # si es 0, se sale sin aprobar nada
    if id_prestamo == 0:
        return
    
    # Buscar el préstamo seleccionado
    prestamo_seleccionado = None
    for prestamo in prestamos_pendientes:
        if prestamo["id"] == id_prestamo:
            prestamo_seleccionado = prestamo
            break
    #si el id no existe pues paila
    if not prestamo_seleccionado:
        log("prestamo seleccionado", "No hay prestamo con ese id", date.today(), "Administrador")
        print("No se encontró un préstamo pendiente con ese ID.")
        return
    
    #mini menu, pq que pereza hacer otro en "menu"
    print("\n¿Qué acción desea realizar?")
    print("1. Aprobar préstamo")
    print("2. Rechazar préstamo")
    
    opcion = validarEntero("Seleccione una opción: ")
    
    if opcion == 1:
        # Aprobar el préstamo
        for prestamo in prestamos:
            if prestamo["id"] == id_prestamo:
                prestamo["estado"] = "prestado"
                # Descontar el stock al aprobar
                for herramienta in herramientas:
                    if herramienta["id"] == prestamo["herramienta_id"]:
                        herramienta["stock"] -= 1
                        break
                break
        guardar(ARCHIVO4, prestamos)
        guardar(ARCHIVO1, herramientas)
        actualizarEstadoPorStock()
        print("\n Préstamo APROBADO correctamente.")
        log("aprobar prestamo", f"se aprobó el préstamo ID {id_prestamo}", datetime.now(), "administrador")
        
    elif opcion == 2:
        # Rechazar el préstamo
        for prestamo in prestamos:
            if prestamo["id"] == id_prestamo:
                prestamo["estado"] = "rechazado"
                mensaje=input("Ingrese la razón del rechazo del prestamo para hacerle saber al residente")
                break
        guardar(ARCHIVO4, prestamos)
        print("\n Préstamo RECHAZADO, se avisará al usuario.")
        log("rechazar prestamo", f"se rechazó el préstamo ID {id_prestamo}", datetime.now(), "administrador")
    else:
        print("Opción inválida.")
        log("prestamo invalido", "puso un numero que no corresponde a ningun prestamo", date.today(), "administrador")
        opcion = validarEntero("Seleccione una opción: ")
#listarPrestamos, que solo me sirve para que el user entre y los vea
def listarPrestamos():
    prestamos = cargar(ARCHIVO4)
    herramientas = cargar(ARCHIVO1)
    usuarios = cargar(ARCHIVO2)
    
    print("\n" + "="*60)
    print("MIS PRÉSTAMOS ACTIVOS")
    print("="*60)
    
    for prestamo in prestamos:
        if prestamo["estado"] == "prestado":
            herramienta = next((h for h in herramientas if h["id"] == prestamo["herramienta_id"]), None)
            usuario = next((u for u in usuarios if u["id"] == prestamo["usuario"]), None)
            if herramienta and usuario:
                print(f"\nID Préstamo: {prestamo['id']}")
                print(f"  Herramienta: {herramienta['nombre']}")
                print(f"  Solicitante: {usuario['nombre']} {usuario['apellido']}")
                print(f"  Fecha Préstamo: {prestamo['fecha_prestamo']}")
                print(f"  Fecha Devolución: {prestamo['fecha_devolucion']}")
                print(f"  Precio: ${prestamo['precio']}")
                print(f"  Observaciones: {prestamo['observaciones']}")