
from gestionUsuariosGeneral import existeResidente
from validaciones import validarEntero,  ValidarCategoria, validarMenu, ValidarNombre
from gestionarJson import cargar, guardar
ARCHIVO = "categorias.json"


# Para saber si la categoria existe o no en el programa, ya que son 3 categorias fijas.
def existeCategoria(nombre_categoria):
    categorias_fijas = ["construccion", "jardineria", "limpieza"]
    return nombre_categoria.lower() in categorias_fijas


    
    