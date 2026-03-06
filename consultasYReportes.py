from gestionHerramientas import ARCHIVO1, listarHerramienta
from gestionPrestamos import ARCHIVO4
from gestionUsuariosGeneral import ARCHIVO2
from gestionarJson import cargar
from datetime import datetime

# 1. Herramientas con stock bajo (menos de 3)
def HerramientasConStockBajo():
    herramientas = cargar(ARCHIVO1)
    herramientas_bajas = [h for h in herramientas if h.get("stock", 0) < 3]
    
    if not herramientas_bajas:
        print("No hay herramientas con stock bajo.")
        return
    
    print("\n" + "="*60)
    print("HERRAMIENTAS CON STOCK BAJO (menos de 3 unidades)")
    print("="*60)
    print(f"{'ID':<5} {'Nombre':<20} {'Categoría':<15} {'Stock':<8} {'Estado':<12}")
    print("="*60)
    for h in herramientas_bajas:
        print(f'{h["id"]:<5} {h["nombre"]:<20} {h["categoria"]:<15} {h["stock"]:<8} {h["estado"]:<12}')
    print("="*60 + "\n")

# 2. Préstamos activos y vencidos (para admin)
def PrestamosActivosyVencidos():
    prestamos = cargar(ARCHIVO4)
    herramientas = cargar(ARCHIVO1)
    usuarios = cargar(ARCHIVO2)
    
    prestamos_activos = [p for p in prestamos if p["estado"] == "prestado"]
    
    if not prestamos_activos:
        print("No hay préstamos activos.")
        return
    
    print("\n" + "="*80)
    print("PRÉSTAMOS ACTIVOS Y VENCIDOS")
    print("="*80)
    print(f"{'ID':<5} {'Herramienta':<20} {'Usuario':<20} {'F. Préstamo':<12} {'F. Devolución':<12} {'Estado':<10}")
    print("-"*80)
    
    fecha_actual = datetime.now()
    
    for prestamo in prestamos_activos:
        herramienta = next((h for h in herramientas if h["id"] == prestamo["herramienta_id"]), None)
        usuario = next((u for u in usuarios if u["id"] == prestamo["usuario"]), None)
        
        if herramienta and usuario:
            # Verificar si está vencido
            try:
                fecha_dev = datetime.strptime(prestamo["fecha_devolucion"], "%Y-%m-%d %H:%M:%S")
            except:
                try:
                    fecha_dev = datetime.strptime(prestamo["fecha_devolucion"], "%Y-%m-%d")
                except:
                    fecha_dev = fecha_actual
            
            if fecha_actual > fecha_dev:
                estado = "VENCIDO"
            else:
                estado = "Activo"
            
            print(f'{prestamo["id"]:<5} {herramienta["nombre"]:<20} {usuario["nombre"] + " " + usuario["apellido"]:<20} {prestamo["fecha_prestamo"]:<12} {prestamo["fecha_devolucion"]:<12} {estado:<10}')
    print("="*80 + "\n")

# 3. Historial de préstamos por usuario (para admin y residente)
def HistorialPrestamosPorUsuario(usuario_id=None):
    prestamos = cargar(ARCHIVO4)
    herramientas = cargar(ARCHIVO1)
    usuarios = cargar(ARCHIVO2)
    
    # Si no se proporciona usuario_id, el admin puede buscar cualquier usuario
    if usuario_id is None:
        usuario_id = int(input("Ingrese el ID del usuario: "))
    
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario:
        print("Usuario no encontrado.")
        return
    
    prestamos_usuario = [p for p in prestamos if p["usuario"] == usuario_id]
    
    if not prestamos_usuario:
        print(f"No hay préstamos para el usuario {usuario['nombre']} {usuario['apellido']}.")
        return
    
    print("\n" + "="*80)
    print(f"HISTORIAL DE PRÉSTAMOS - {usuario['nombre']} {usuario['apellido']}")
    print("="*80)
    print(f"{'ID':<5} {'Herramienta':<20} {'F. Préstamo':<12} {'F. Devolución':<12} {'Precio':<10} {'Estado':<12}")
    print("-"*80)
    
    for prestamo in prestamos_usuario:
        herramienta = next((h for h in herramientas if h["id"] == prestamo["herramienta_id"]), None)
        if herramienta:
            print(f'{prestamo["id"]:<5} {herramienta["nombre"]:<20} {prestamo["fecha_prestamo"]:<12} {prestamo["fecha_devolucion"]:<12} ${prestamo["precio"]:<9} {prestamo["estado"]:<12}')
    print("="*80 + "\n")

# 4. Herramientas más solicitadas (para admin)
def HerramientasMasSolicitadas():
    prestamos = cargar(ARCHIVO4)
    herramientas = cargar(ARCHIVO1)
    
    # Contar préstamos por herramienta
    conteo = {}
    for prestamo in prestamos:
        herramienta_id = prestamo["herramienta_id"]
        if herramienta_id in conteo:
            conteo[herramienta_id] += 1
        else:
            conteo[herramienta_id] = 1
    
    # Ordenar por cantidad de préstamos
    herramientas_ordenadas = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    
    if not herramientas_ordenadas:
        print("No hay préstamos registrados.")
        return
    
    print("\n" + "="*60)
    print("HERRAMIENTAS MÁS SOLICITADAS")
    print("="*60)
    print(f"{'Posición':<10} {'Herramienta':<25} {'Cantidad de Préstamos':<20}")
    print("-"*60)
    
    for i, (herramienta_id, cantidad) in enumerate(herramientas_ordenadas, 1):
        herramienta = next((h for h in herramientas if h["id"] == herramienta_id), None)
        if herramienta:
            print(f'{i:<10} {herramienta["nombre"]:<25} {cantidad:<20}')
    print("="*60 + "\n")

# 5. Usuarios que solicitan más (para admin)
def UsuariosQueSolicitanMas():
    prestamos = cargar(ARCHIVO4)
    usuarios = cargar(ARCHIVO2)
    
    # Contar préstamos por usuario
    conteo = {}
    for prestamo in prestamos:
        usuario_id = prestamo["usuario"]
        if usuario_id in conteo:
            conteo[usuario_id] += 1
        else:
            conteo[usuario_id] = 1
    
    # Ordenar por cantidad de préstamos
    usuarios_ordenados = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    
    if not usuarios_ordenados:
        print("No hay préstamos registrados.")
        return
    
    print("\n" + "="*60)
    print("USUARIOS QUE SOLICITAN MÁS HERRAMIENTAS")
    print("="*60)
    print(f"{'Posición':<10} {'Usuario':<30} {'Cantidad de Préstamos':<20}")
    print("-"*60)
    
    for i, (usuario_id, cantidad) in enumerate(usuarios_ordenados, 1):
        usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
        if usuario:
            nombre_completo = f"{usuario['nombre']} {usuario['apellido']}"
            print(f'{i:<10} {nombre_completo:<30} {cantidad:<20}')
    print("="*60 + "\n")

