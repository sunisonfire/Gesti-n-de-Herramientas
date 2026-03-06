# PROYECTO: Gestion de Herramientas 🔧🔨

## Lenguaje empleado 🌐: Python 
ˆ𐃷ˆ ˆ𐃷ˆ ˆ𐃷ˆ ˆ𐃷ˆ ˆ𐃷ˆ ˆ𐃷ˆ ˆ𐃷ˆ ˆ𐃷ˆ ˆ𐃷ˆ ˆ𐃷ˆ ˆ𐃷ˆ 

## 💬 Descripcion del problema:

*En muchos barrios existe la costumbre de compartir herramientas entre vecinos para evitar que cada persona tenga que comprarlas todas. El problema es que, con el tiempo, se pierde el control: algunas herramientas no se devuelven a tiempo, otras se dañan y no se sabe quién las tiene, o simplemente no hay registro claro de cuántas hay disponibles.*

## 🏷️ Planteo de solución:

*La junta comunal de tu barrio ha decidido organizar este proceso mediante un programa de consola que registre las herramientas, los vecinos y los préstamos realizados. Con esta solución, esperan que cualquier integrante de la comunidad pueda consultar la información sin depender de cuadernos ni llamadas telefónicas* 

## 🚩 Requermientos:

**👔 - Perfil Administrador:**  

- Agregar productos
- Actualizar precio y stock
- Eliminar productos
- Ver inventario
- Gestionar distribución

**🧑‍💻 - Perfil Usuario:**  
- Ver catálogo de productos
- Consultar precios
- Consultar disponibilidad
- Realizar solicitudes de compra

## 🗃️- Estructura: ദ്ദി •⩊• )

_Se presenta una estructura modulada con gestion de herramientas y gestion de usuarios como muestro a continuacion:_

_🦖1. Se crea una contraseña para el ingreso del administrador al programa:_

```
contraseña_real=1009
```
_🦖 2. Se crea un menú general que lleve a un menú ya sea de administrador (que se abre si la contraseña que ingresa es igual a la contraseña real) o el de usuario_

```
def menuPrincipal():
    while True:
        print("""
        =====================================
        BIENVENIDO AL CONTROL DE HERRAMIENTAS
        =====================================""")
        op=validarMenu('''
                            1. Administrador
                            2. Residente
                            ''',1,2)
        while op==None:
            op=validarMenu('Error, intente nuevamente!',1,2)
        if op==1:
            menuAdministrador()
        if op==2:
            menuResidente()
        else:
            print("Error, número no válido")
            log("Número no válido","El usuario ha puesto un número que no se encuentra en el menú",date.today(), "Usuario no ha iniciado sesión")
```

_🦖 3. Tras ingresar al menú de administradores se encuentra con diferentes comandos que pueden llevarlo a acciones que el administrador puede controlar_

```
def menuAdministrador():
    contraseña_real=1009
    contraseña=int(input("Ingrese la contraseña: "))
    if contraseña!=contraseña_real:
        print("Contraseña incorrecta. Acceso denegado.")
        return
    else:
        print("¡Bienvenido, Administrador!")
    while True:
        op7=validarMenu('''
                    =====================
                    ¿Qué desea gestionar?
                    =====================
                    
                    1. Gestionar Herramientas
                    2. Gestionar Residentes
                    3. Gestionar Préstamos
                    4. Consultas y Reportes
                    5. Salir
                    ''',1,5)
        if op7==1:
                menuAdministradorHerramientas()
        elif op7==2:
                menuAdministradorResidentes()
        elif op7==3:
                aprobarRechazarPrestamos()
        elif op7==4:
                consultasYReportes()                
        else:
            log("Número no validado","El usuario ha puesto un número fuera del menú y se ha devuelto al menú principal", date.today(), "administrador" )
            break
```

_🦖 4. Al igual que el administrador, el usuario final podrá ingresar a su propio menu para consultar las herramientas disponibles, para consultar los prestamos que tiene activos, y para pedir un nuevo prestamo, entre mas funciones_

```
def menuResidente():
    while True:
        usuario=int(input("Ingrese su id de residente: "))
        elemento=obtenerResidentePorId(usuario)
        if not elemento:
                log("id incorrecto", "se ingresa id inexistente", date.today())
                print("ID de usuario incorrecto. Acceso denegado.")
                return
        else:
                print(f"¡Bienvenido, {elemento['nombre']} {elemento['apellido']}!")
        op5=validarMenu('''
                    ==================
                    ¿Qué desea hacer?  
                    ==================
                        
                    1. Solicitar Préstamo
                    2. Ver mis préstamos
                    3. Salir
                    ''',1,3)
        if op5==1:
                solicitarPrestamos()
        elif op5==2:
                solicitudesPendientes()
        else: 
            log("menu residente", "se ingreso numero fuera del menu", date.today())
            break
        
```

_🦖 5. En cuanto los usuarios ingresen en sus menús, se valida que el numero que escriba sea correcto, de lo contrario una de las validaciones correspondiente se los hará saber_

```
def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None

def validarMenu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None

def existeCategoria(nombre_categoria):
    lista_categorias = cargar("categorias.json")
    for elemento in lista_categorias:
        if elemento["categoria_escogida"].lower() == nombre_categoria.lower():
            return True
    return None

def validarHerramienta(nombre_herramienta):
    if nombre_herramienta.strip()=="":
        print("Nombre vacio")
        log("herramienta vacio", "nombre vacio", date.today(), "usuario")
        return False
    return True

def ValidarCategoria(categoria):
    if categoria.strip()=="":
        print("Categoría vacio")
        log("categoria vacio", "vacio", date.today(), "usuario")
        return False
    return True

def ValidarNombre(categoria):
    if categoria.strip()=="":
        print("Nombre vacio")
        log("nombre vacio", "nombre vacio", date.today(), "usuario")
        return False
    return True


```

## 🦺 - Historial de acciones o LOGS: ˶ˊᜊˋ˶

_Descripción: Archivo informático que registra secuencialmente y de forma automática los eventos, acciones y errores de un sistema, aplicación o servidor._

_Uso: Se emplea para que el administrador pueda ver el recorrido del usuario y además notar los errores que se suelen cometer a la hora de interactuar con la app_

```
def log(accion, descripcion, fecha, usuario):
    ARCHIVO = "logs.json"
    lista=cargar(ARCHIVO)
    lista.append({
        "id": generar_id(lista),
        "accion": accion,
        "descripcion": descripcion,
        "fecha": str(fecha),
        "usuario": usuario,
    })
    guardar(ARCHIVO, lista)

```

## 🧐- Especificaciones: ˃ 𖥦 ˂

- _Este sistema solo puede trabajar con las herramientas que el administrador agregue previamente, en caso de que un usuario quiera agregar una, no será posible, solo el administrador tiene acceso_

- _Al momento de devolver una herramienta se le pedirá al administrador el estado de esta, con el fin de prestar solo aquellas que cuentan con un buen estado_

- _Si el usuario al que se le prestó la herramienta no la ha devuelto al finalizar la fecha límite, se le sumará mora por cada día que pase_

## 💫 - Ejecución: 𖦹 ´ ᯅ ` 𖦹
- _La persona ingresa que tipo de usuario es: Administrador, Residente._
- _Según el tipo, es enviado a dos menús distintos, siendo administrador valida la contraseña para entrar, de lo contrario lo devuelve al menú._
- _Se validan los datos ingresados y se manda un mensaje en caso de datos erroneos_
-_El fin del programa no llega, a menos que en el menú principal se tome la opción 3, Salir._
- _Puede manejar herramientas y usuarios, o prestamos y devoluviones siendo administrador._
- _Como residente puede pedir prestamos que serán aprobados o rechazados por el administrador_
- _Podrá ver los usuarios que más piden herramientas y las herramientas más pedidas por los usuarios_


## 👽️ - Estado del proyecto:

🚨_Finalizado_🚨
⠀⠀⠀⠀⠀⣶⡀⠀⠀⠀⣰⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀
⠀⣀⠀⠀⠀⠉⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢋⠆⣿⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⢻⡇⠀
⠀⠙⠳⠀⠀⣠⡴⠞⠓⠲⢦⡀⠀⠠⠞⠃⠀⠀⠀⠀⠀⣠⠟⠁⠌⠀⢸⡇⠀⠀⠀⢀⣠⡶⠛⠁⢀⠘⣧⠀
⠀⠀⠀⠀⣼⠋⠀⠀⠀⢀⠀⢻⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⡌⠀⠤⢤⣿⣤⣤⠶⠛⠁⠀⠀⠀⡌⠀⣿⠀
⢠⣤⠄⠀⣿⠀⠀⡄⠀⢨⠀⣾⠀⠀⠀⠀⠀⠀⣰⠞⡁⠄⠂⠁⠀⠀⠈⠉⠉⢍⠀⠀⠀⠀⠀⢀⠃⠀⣿⠀
⠀⠀⠀⠀⠘⠳⣤⣌⣤⣬⣾⡁⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠄⠀⠀⠀⡌⠀⠀⣻⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢷⣿⣿⣷⡀⠀⠀⣼⣯⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠒⠁⠀⠀⣹⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠗⠀⠀⣼⣣⣦⡌⠙⠀⠀⠀⠀⠀⠀⠀⠶⠶⠶⠶⠤⣄⣀⠀⠀⠀⠀⠀⢹⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠏⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣶⡄⠈⠛⠀⠀⠀⠀⢹⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠿⠃⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢁⣀⠐⠀⢿⣀⣠⣦⡀⠀⠀⠀⢸⡆⠈⠁⠀⠒⠂⠠⡀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠸⡏⠁⠈⠙⠓⢲⠞⠉⠀⠂⠤⠀⠀⠀⠤⠃⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢿⡄⠀⠀⠀⠀⠳⣄⡀⢀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⣴⠛⠉⢳⡄⠙⠳⢦⣄⣀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠈⢷⡀⠀⠀⠈⠉⠛⢻⡶⠶⢤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⡴⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠈⢳⣤⣤⣤⠶⠖⣿⠃⠀⠀⠀⠀⠀⠉⠉⢹⣏⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠈⠙⠉⠉⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣤⣀⣠⣤⡴⠖⢻⡏⠀⠀⠀⠀⠀⠀⠀⢶⣄⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⣸⠻⢦⡀⠀⠈⠻⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠀⣰⠟⠀⠀⢀⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠐⠛⠁⠀⠀⠀⠀

## 🚧 - Pendientes: 𐔌՞. .՞𐦯
_El proyecto tiene una falla en los logs que no ha sido finalizada, además le falta la parte de devoluciones para que el usuario pueda devolver la herramienta sin necesidad del control del admin_

## 🔥 Autor:
                    @sunisonfire
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⠉⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠈⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠹⣷⡄⠀⠀⠀⠀⠀⣠⡾⠇⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠄⠈⠌⢿⣦⣤⣤⣤⣴⠟⠡⠀⠀⠠⠀⠘⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⡟⠀⠀⢂⠄⠊⠀⠀⠉⠁⠀⠈⠉⠀⠀⠐⠠⡀⠀⠀⠹⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⡿⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⢻⣧⠀⠀⠀⠀
⠀⠀⠀⢀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀
⠀⢀⣀⣼⣷⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣼⣧⡀⠀⠀
⣴⣿⠟⠉⠁⢠⣾⣿⣯⠙⠛⠛⠉⠙⠻⣿⡿⠿⢿⣿⣿⠟⠛⠉⣿⣿⣿⡟⠛⠛⢿⣿⡄
⣿⣿⡄⠀⠀⠸⣿⣿⡿⠁⠀⠀⠀⠀⣠⣿⠁⠀⠀⠹⣿⣄⠀⠀⢿⣿⣿⠟⠀⠀⠀⣿⠇
⠈⠻⣿⣷⣶⣤⣤⣤⣤⣤⣤⣤⣴⡾⠿⠃⠀⠀⠀⠀⠈⠻⠿⢶⣶⣾⣧⣤⣤⡶⣿⠛⠀
⠀⠀⣿⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠦⡄⠀⠀⠀⠀⠀⠀⠈⠀⢻⡆⠀
⠀⠀⣿⠀⠁⠀⠀⠀⠀⠂⠀⠀⣾⣁⣤⢷⣄⣀⣀⣀⡴⠃⠀⠀⠀⠀⠀⠀⠈⠀⢸⡇⠀
⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠈⠉⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠃⠀
⠀⠀⠈⠛⠷⣶⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣠⣤⣶⠶⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀

## 👥 - CONTACTO:

ykremysun@gmail.com

![Texto Alt](https://i.pinimg.com/736x/70/3e/69/703e69fff1436ea82f18c369696a80a3.jpg)
