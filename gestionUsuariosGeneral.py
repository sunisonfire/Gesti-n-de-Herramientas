from gestionarJson import cargar, guardar, generar_id
from validaciones import validarEntero, ValidarNombre
from datetime import date
from historialAcciones import log

ARCHIVO2 = "usuarios.json"

#pa cuando se busque y eso
def existeResidente(usuario):
    #se lista los que hay
    lista_usuarios=cargar(ARCHIVO2)
    #se busca entre los que hay
    for elemento in lista_usuarios:
        if usuario==elemento["id"]:
            return True
    return None

#crear residente
def agregarResidente():
    #cicloo
    while True:
        usuarios=cargar(ARCHIVO2)
        print(" REGISTRO DE NUEVO USUARIO ")

        #se ingresan los datos
        nombre=input("Ingresa el nombre del residente: ")
        while ValidarNombre(nombre)==False:
            nombre=input("Error, ingresa un residente valido: ")

        apellido=input("Ingresa el apellido del residente: ")
        while ValidarNombre(apellido)==False:
            apellido=input("Error, ingresa un apellido valido: ")

        telefono=validarEntero("Ingresa el numero de telefono del residente (10 digitos):  ")
        while telefono is None or telefono<1111111111:
            telefono=validarEntero("Error, ingresa un numero de telefono valido (10 digitos):  ")

        direccion=input("Ingresa la direccion del residente: ")
        while not direccion or len(direccion.strip())==0:
            direccion=input("Error, ingresa una direccion valida: ")

        #se meten en el json
        nuevo_residente={
            "id": generar_id(usuarios) ,
            "nombre": nombre,
            "apellido":apellido,
            "telefono": telefono,
            "direccion": direccion,
            "tipoUsuario":"Residente"
        }
        usuarios.append(nuevo_residente)
        guardar(ARCHIVO2,usuarios)
        print(f'¡{nombre}, guardad@ en el sistema!')

        #se registra la accion en el historial
        log("agregar usuario", "se agregó un nuevo usuario al sistema", date.today(), "usuario_actual")
        input('Presione Enter para volver al menú principal...')
        break

#cambiar datos del residente, excepto el id, y el tipo de usuario, que es residente
def actualizarResidente():
    usuarios=cargar(ARCHIVO2)
    listarResidente()
    usuario=validarEntero("Escoja el id a actualizar")
    while(usuario==None):
        usuario=validarEntero("Error, escoja el id a actualizar")
        
    for elemento in usuarios:
        if usuario==elemento["id"]:
            nombre=input("Ingrese el nuevo nombre del residente: ")
            while ValidarNombre(nombre)==False:
                nombre=input("Error, ingresa un residente valido: ")

            apellido=input("Ingrese el nuevo apellido del residente: ")
            while ValidarNombre(apellido)==False:
                apellido=input("Error, ingresa un apellido valido: ")

            telefono=validarEntero("Ingrese el nuevo numero de telefono del residente (10 digitos):  ")
            while telefono is None or telefono<1111111111:
                telefono=validarEntero("Error, ingresa un numero de telefono valido (10 digitos):  ")

            direccion=input("Ingrese la nueva direccion del residente: ")
            while not direccion or len(direccion.strip())==0:
                direccion=input("Error, ingresa una direccion valida: ")

            #lo modificamos y guardamos en el json
            elemento["nombre"]=nombre
            elemento["telefono"]=telefono
            elemento["direccion"]=direccion
            guardar(ARCHIVO2, usuarios)
            print('¡Residente actualizado!')
            log("actualizar usuario", "se actualizó un usuario en el sistema", date.today(), nombre)
            return
    print("El residente no existe. \n")

#pues quitar uno de los que ya estan, solo lo hace un admin
def eliminarResidente():
    contador_aux=0
    usuarios=cargar(ARCHIVO2)
    listarResidente()
    usuario=validarEntero("Escoja el id a eliminar")
    while(usuario==None):
        usuario=validarEntero("Error, escoja el id a eliminar")
        
        #se hace un .pop 
    for elemento in usuarios:
        if usuario==elemento["id"]:
            usuarios.pop(contador_aux)
            guardar(ARCHIVO2, usuarios)
            print('Residente eliminado!')
            return
        contador_aux+=1
    print("El residente no existe. \n")

#se busca residente por id
def buscarResidente():
    usuarios=cargar(ARCHIVO2)
    usuario=validarEntero("Ingrese el ID del residente que desea buscar: ")
    while(usuario==None):
        usuario=validarEntero("Error, ingrese un ID válido: ")
    
    #se lista residente
    for elemento in usuarios:
        if usuario==elemento["id"] and elemento["tipoUsuario"]=="Residente":
            print(f'ID: {elemento["id"]} -> Nombre: {elemento["nombre"]} Apellido: {elemento["apellido"]} -> Telefono: {elemento["telefono"]} -> Direccion: {elemento["direccion"]}')
            return elemento
    print("No se encontró un residente con ese ID.")
    log("buscar residente", "se buscó un residente en el sistema", date.today(), "usuario_actual")

#Retorna el objeto del residente dado su ID, o None si no existe
def obtenerResidentePorId(usuario):
    usuarios=cargar(ARCHIVO2)
    for elemento in usuarios:
        if usuario==elemento["id"] and elemento["tipoUsuario"]=="Residente":
            return elemento
    return None

#se hace la lista de todos los que hay, pero la hice bonita con los = y el espaciado
def listarResidente():
    usuarios=cargar(ARCHIVO2)

    if not usuarios:
        print ("No hay residentes guardados\n")
        return
    else:
        print("="*80)
        print(f"{'ID':<5} {'Nombre':<20} {'Apellido':<15} {'Telefono':<12} {'Direccion':<10}")
        print("="*80)
        for elemento in usuarios:
            print(f'{elemento["id"]:<5} {elemento["nombre"]:<20} {elemento["apellido"]:<15} {elemento["telefono"]:<12} {elemento["direccion"]:<10}')
            print("="*80)
            log("listar residente", "se muestran los residentes", date.today(), "usuario_actual")  