from gestionarJson import cargar, guardar, generar_id

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