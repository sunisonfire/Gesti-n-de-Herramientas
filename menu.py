from validaciones import validarMenu
from gestionHerramientas import actualizarHerramienta, buscarHerramienta, eliminarHerramienta, agregarHerramienta, listarHerramienta    
from gestionUsuariosGeneral import buscarResidente, listarResidente, eliminarResidente, actualizarResidente, agregarResidente, obtenerResidentePorId
from gestionPrestamos import solicitarPrestamos, solicitudesPendientes, aprobarRechazarPrestamos
from consultasYReportes import  HerramientasConStockBajo, PrestamosActivosyVencidos, HistorialPrestamosPorUsuario,UsuariosQueSolicitanMas, HerramientasMasSolicitadas
from historialAcciones import historialAcciones, log
from datetime import date

#menu de admin o residente
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

#menu de herramientas, residentes o prestamos   
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

#menu de agregar, eliminar, buscar... herramientas ADM
def menuAdministradorHerramientas():
    while True:
            op1=validarMenu('''
                            =========================
                            1. Agregar Herramienta
                            2. Actualizar Herramienta
                            3. Eliminar Herramienta
                            4. Listar Herramientas
                            5. Buscar por ID
                            6. Salir
                            =========================
                            ''',1,6)
            while op1==None:
                    op1=validarMenu('Error, intente nuevamente!',1,6)
                    log("Número no validado","El usuario no ha puesto nada", date.today(), "Administrador")
            match op1:
                case 1:
                    agregarHerramienta()
                case 2:
                    actualizarHerramienta()
                case 3:
                    eliminarHerramienta()
                case 4:
                    listarHerramienta()
                case 5:
                    buscarHerramienta()
                case 6:
                    print('Gracias por usar nuestro servicio')
                case _:
                    print('No se encontró la opción.')
                    log("Número no validado","El usuario ha puesto un número fuera del menú", date.today(), "Administrador")
            if op1==6:
                log("Número no validado","El usuario ha puesto un número fuera del menú", date.today(), "Administrador")
                break

#menu de agregar, eliminar, buscar... usuarios ADM
def menuAdministradorResidentes():
    while True:
            op2=validarMenu('''
                            =========================
                            1. Agregar Residente
                            2. Actualizar Residente
                            3. Eliminar Residente
                            4. Listar Residentes
                            5. Buscar Residente
                            6. Salir
                            =========================
                            ''',1,6)
            while op2==None:
                    log("menu administrador", "no se ingresa opcion", date.today(), "admin")
                    op2=validarMenu('Error, intente nuevamente!',1,6)
            match op2:
                case 1:
                    agregarResidente()
                    return
                case 2:
                    actualizarResidente()
                case 3:
                    eliminarResidente()
                case 4:
                    listarResidente()
                case 5:
                    buscarResidente()
                case 6:    
                    print('Gracias por usar nuestro servicio')
                case _:
                    print('No se encontró la opción.')
                    log("menu administrador", "no se ingresa opcion", date.today(), "admin")
            if op2==6:
                log("menu administrador", "no se ingresa opcion", date.today(), "admin")
                break

#menu de solicitar y ver prestamos RESIDENTE
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
        
#menu de consultas y resportes ADMIN
def consultasYReportes():
    while True:
        op8=validarMenu('''
                    =====================
                    ¿Qué desea gestionar?
                    =====================
                    
                    1. Herramientas con Stock bajo
                    2. Prestamos activos y vencidos
                    3. Usuarios que más solicitan
                    4. Herramientas más solicitadas
                    5. Historial 
                    6. Salir
                    ''',1,6)
        if op8==1:
                HerramientasConStockBajo()
        elif op8==2:
                PrestamosActivosyVencidos()
        elif op8==3:
                HistorialPrestamosPorUsuario()
        elif op8==4: 
                HerramientasMasSolicitadas()     
        elif op8==5:
                historialAcciones()
        elif op8==6:
            break
        else:
            print("Ingrese una opción válida")
            log("en consultas y reportes", "se ha ingresado un numero fuera del menu", date.today(), "admin")
            break