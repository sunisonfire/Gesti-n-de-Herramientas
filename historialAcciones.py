from gestionarJson import cargar, guardar, generar_id

def historialAcciones():
    """Muestra la lista de acciones del historial tal cual está en el JSON"""
    ARCHIVO = "logs.json"
    lista = cargar(ARCHIVO)
    
    if not lista:
        print("No hay acciones en el historial.")
        return
    
    print("\n" + "="*60)
    print("         HISTORIAL DE ACCIONES")
    print("="*60)
    for item in lista:
        print(f"\nID: {item.get('id', 'Error, id no válidado')}")
        print(f"Acción: {item.get('accion', 'No hay acción')}")
        print(f"Descripción: {item.get('descripcion', 'No hay descripción')}")
        print(f"Fecha: {item.get('fecha', 'Fecha no válidada')}")
        print(f"Usuario: {item.get('usuario', 'Sin usuario')}")
        print("-" * 40)
    print("\n" + "="*60)

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