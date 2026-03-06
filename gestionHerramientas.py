from gestionarJson import cargar, guardar, generar_id
from validaciones import validarEntero, validarHerramienta, ValidarCategoria, ValidarNombre
from historialAcciones import log   
from datetime import date, datetime, timedelta
from gestionCategoria import existeCategoria

ARCHIVO1 = "herramienta.json"

#cuando el stock sea 0, el estado automáticamente será prestado
def actualizarEstadoPorStock():
    herramientas = cargar(ARCHIVO1)
    for herramienta in herramientas:
        if herramienta.get("stock", 0) == 0:
            herramienta["estado"] = "prestado"
        elif herramienta.get("stock", 0) > 0 and herramienta.get("estado") == "prestado":
            herramienta["estado"] = "disponible"
    guardar(ARCHIVO1, herramientas)

#Agregar una herramienta desde 0
def agregarHerramienta():
    #se carga json de la herramienta
    herramientas=cargar(ARCHIVO1)

    nombre_herramienta = input('Ingrese el nombre de la herramienta: ')
    while not validarHerramienta(nombre_herramienta):
        log("nombre invalido", "nombre de la herramienta invalido", date.today(), "administrador")
        nombre_herramienta = input('Ingrese el nombre valido para la herramienta: ')

    #damos la opcion de escoger las categorias, pero para ahorrar codigo, el usuario debe escribir la categoria
    categoria_escogida = input('''
        =======================================
        Escriba la categoria de la herramienta:
        =======================================
        Construccion
        Jardineria
        Limpieza
        >
        ''').strip().lower()
    #strip para no tener espaciados, y lower para leerla en minuscula

    while not existeCategoria(categoria_escogida):
        log("No existe categoria","El usuario ha puesto una categoria inexistente", date.today(), "Administrador")
        categoria_escogida = input('Error, la categoria no existe. Ingrese nuevamente: ').strip().lower()

    #pedimos la cantidad de herramientas que se va a agregar aqui
    stock_herramienta = validarEntero('Ingrese el stock de la herramienta: ')
    while stock_herramienta is None:
        log("Número inexistente","El usuario ha dejado un campo vacio", date.today(), "Administrador")
        stock_herramienta = validarEntero('Error, ingrese el stock de la herramienta: ')

    #el precio de alquiler varia segun la herramienta, y se le suma el precio base que cuenta por dias
    precio_alquiler = validarEntero('Ingrese el precio de alquiler de la herramienta: $')
    print("el precio base del alquiler es de $2000 por dia sumado a el precio anteriormente ingresado")
    while precio_alquiler is None:
        log("Número no validado","El usuario ha dejado el precio en blanco", date.today(), "Administrador")
        precio_alquiler = validarEntero('Error, ingrese el precio de alquiler de la herramienta: $')
        

    #creamos el diccionario:3
    nueva_herramienta = {
        "id": generar_id(herramientas),
        "nombre": nombre_herramienta,
        "categoria": categoria_escogida,
        "precio de alquiler": precio_alquiler,
        "estado": "disponible",
        "stock": stock_herramienta,
        "prestamos": "devuelta"
    }
    #guardamos los datos con append en el json
    herramientas.append(nueva_herramienta)
    guardar(ARCHIVO1, herramientas)
    actualizarEstadoPorStock()
    print('¡Nueva herramienta guardada!')
    #pasamos el historial de lo que acabamos de hacer con un log
    log("agregar herramienta", "se crea una herramienta", datetime.now(), "Administrador")
    input('Presione Enter para volver al menú...')

#esto se muestra al admin para que cuando le devuelan una herramienta, este pueda cambiar el estado,
#pero además decimos que si no se tiene registrado un estado antes, será disponible (o sea recien agg la herramienta)
def estadoHerramienta():
        if estado_herramienta==None:
            estado_herramienta="disponible"
        else:
            estado_herramienta = ValidarCategoria('''
                                        =======================================
                                        Ingrese el estado de la herramienta:
                                        =======================================
                                        Disponible 
                                        Ocupada
                                        Reparacion
                                        >
                                        ''').strip()

#hacemos la lista de lo que hay, se usa el "="*80 para poner 80 cositos
#y se pone <20 para poner los espacios entre titulos
def listarHerramienta():
    herramientas=cargar(ARCHIVO1)

    if not herramientas:
        print ("No hay herramientas registradas\n")
        return

    print("="*80)
    print(f"{'ID':<5} {'Nombre':<20} {'Categoría':<15} {'Estado':<12} {'Stock':<8} {'Precio':<10}")
    print("="*80)
    for elemento in herramientas:
        print(f'{elemento["id"]:<5} {elemento["nombre"]:<20} {elemento["categoria"]:<15} {elemento["estado"]:<12} {elemento["stock"]:<8} ${elemento["precio de alquiler"]:<9}')
    print("="*80 + "\n")
    log("listar herramienta", "se muestran las herramientas", datetime.now(), "usuario_actual")   

# el .pop y el contador son para eliminar el elemento del json, el pop lo saca y
# el contador es para saber en que posicion del json esta el elemento a eliminar
def eliminarHerramienta():
    contador_aux=0
    herramientas=cargar(ARCHIVO1)
    listarHerramienta()
    id_herramienta=validarEntero("Escoja el ID a eliminar")
    while(id_herramienta==None):
        log("No hay ID","El usuario ha puesto un id vacio", date.today(), "Administrador")
        id_herramienta=validarEntero("Error, escoja el ID a eliminar")
        
    for elemento in herramientas:
        if id_herramienta==elemento["id"]:
            herramientas.pop(contador_aux)
            guardar(ARCHIVO1, herramientas)
            print('¡Herramienta eliminada!')
            return
        contador_aux+=1
    print("La herramienta es inexistente. \n")
    log("eliminar herramienta", "se eliminó una herramienta", datetime.now(), "administrador")   

#buscar una herramienta dentro del json, pero sin tirarlas todas
def buscarHerramienta():
        #herramienta es cada una y herramientas e,l json
        herramientas = cargar(ARCHIVO1)
        
        # Si no se proporciona ID, pedirlo
        id_herramienta = validarEntero("Ingrese el ID de la herramienta a buscar: ")
        while id_herramienta is None:
            id_herramienta = validarEntero("Error, ingrese el ID de la herramienta a buscar: ")
        
        # Buscar la herramienta con el id de esta
        herramienta_encontrada = None
        for herramienta in herramientas:
            if herramienta["id"] == id_herramienta:
                herramienta_encontrada = herramienta
                break

        #tras encontrar la herramienta me botará toda su info basica
        if herramienta_encontrada:
            print("\n""========================")
            print("DATOS DE LA HERRAMIENTA")
            print("========================")
            print(f'ID:              {herramienta_encontrada["id"]}')
            print(f'Nombre:          {herramienta_encontrada["nombre"]}')
            print(f'Categoría:       {herramienta_encontrada["categoria"]}')
            print(f'Precio alquiler: ${herramienta_encontrada["precio de alquiler"]}')
            print(f'Estado:          {herramienta_encontrada["estado"]}')
            print(f'Stock:           {herramienta_encontrada["stock"]}')
            print(f'Préstamo:        {herramienta_encontrada["prestamos"]}')
            print("\n"              "==============================")
            log("buscar herramienta", "se buscó una herramienta por ID", datetime.now(), "usuario_actual")
        else:
            print("No se encontró una herramienta con ese ID.")
            log("buscar herramienta", "intento buscar herramienta inexistente", datetime.now(), "usuario_actual")

#como esta opcion solo la tiene el admin, se '''confiará''' que solo quiere cambiar el estado a dañada,
# pero iigualmente podra a disponible o prestada, aunque eso ya es automatico
#por otra parte, no se va a pedir cambiar el nombre, ni el stock, ni nada directamente.
def actualizarHerramienta():
        herramientas = cargar(ARCHIVO1)
        listarHerramienta()
        id_herramienta = validarEntero("Ingrese el ID de la herramienta a actualizar: ")
        for herramienta in herramientas:
            if herramienta["id"] == id_herramienta:
                print(f"Actualizando herramienta: {herramienta['nombre']}")
                print("Estados posibles: 1. Disponible  2. Dañada  3. Prestada")
                estado = validarEntero("Ingrese el nuevo estado (1-3): ")
                if estado == 1:
                    herramienta["estado"] = "disponible"
                    herramienta["prestada"] = ""
                elif estado == 2:
                    herramienta["estado"] = "dañada"
                    herramienta["prestada"] = ""
                elif estado == 3:
                    herramienta["estado"] = "prestada"
                    listarHerramienta
                else:
                    print("Estado no válido.")
                    return
                guardar(ARCHIVO1, herramientas)
                print("¡Herramienta actualizada!")
                return
        print("No se encontró la herramienta con ese ID.")
        log("actualizar herramienta", "no se actualizó una herramienta", datetime.now(), "administrador")