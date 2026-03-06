from gestionarJson import cargar
from historialAcciones import log
from datetime import date
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

