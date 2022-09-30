from persona import persona
misContactos = [persona(101,'Luis','Casa 1'),persona(102,'Pedro','Casa 2')]

def crearContacto(numero, nombre, direccion):
    misContactos.append(persona(numero, nombre, direccion))
    print("Contacto almacenado.")

def buscarContacto(nombre):
    
    if len(misContactos)==0:
        print("La lista está vacía; no hay contactos que buscar.")
    else:
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        encontrado = False
        for i in range (len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                print("El teléfono es:",misContactos[i].verNumero())
                print("La dirección es:",misContactos[i].verDireccion())
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado == False:
            print("Dato no existente.")


def mostrarContactos():
    if len(misContactos) == 0:
        print("La lista está vacía.")
    else:
        print('------------------------------------')
        for i in range (len(misContactos)):
            print(' Nombre:', misContactos[i].verNombre(),'\n',
            'Dirección:',misContactos[i].verDireccion(),'\n',
            'Teléfono:',misContactos[i].verNumero(),'\n',
            '------------------------------------')


def modificarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista está vacía.")
    else:
        encontrado: False
        posicion: None
        for i in range (len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                posicion = i
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado == True:
            nuevoNumero = int(input('Ingrese el nuevo número: '))
            nuevoNombre = input('Ingrese un nuevo nombre: ')
            nuevaDireccion = input('Ingrese una nueva dirección: ')
            misContactos[posicion].modificarNumero(nuevoNumero)
            misContactos[posicion].modificarNombre(nuevoNombre)
            misContactos[posicion].modificarDireccion(nuevaDireccion)
            print('Datos actualizados con éxito.')
        else:
            print('Dato no encontrado.')


def eliminarContacto(nombre):
    if len(misContactos) == 0:
        print('La lista está vacía.')
    else:
        encontrado = False
        posicion = None
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                posicion = i
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado:
            misContactos.pop(posicion)
            print('Contacto eliminado con éxito.')

def crearReporte():
    documento = open ("reporte contactos.html","w")
    documento.write("<!doctype html>\n <html>\n")
    documento.write("<head>\n")
    documento.write("\t<title>Agenda 2022</title>\n")
    documento.write("</head>\n")
    documento.write("<body>\n")
    documento.write("<center> <h1>Mis contactos</h1>\n")
    documento.write('\t<table border="1">\n')
    documento.write("\t\t<tr>\n")
    documento.write("\t\t\t<td>Número de Teléfono</td><td>Nombre</td><td>Dirección</td>\n")
    documento.write("\t\t</tr>\n")
    for i in range (len(misContactos)):
        documento.write(
            "\t\t<tr>"+
            "\t\t\t<td>"+str(misContactos[i].verNumero())+"</td>"+
            "<td>"+misContactos[i].verNombre()+"</td>"+
            "<td>"+misContactos[i].verDireccion()+"</td>"+
            "\t\t</tr>")
        print('</center>')
    documento.write("</body>\n")
    documento.write("</html>")
    documento.close()
    print('Reporte creado con éxito.')

def main():
    op = 0
    print("------------------------AGENDA 2022-----------------------")
    while op != 7:
        print('__________________________________________________________')
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Ver todos los contactos")
        print("4. Modificar contacto")
        print("5. Eliminar contacto")
        print("6. Crear reporte en HTML")
        print("7. Salir")
        op = int(input("ingrese el número de opción: "))
        if op == 1:
            numero = int(input("Ingrese el número de teléfono: "))
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la dirección: ")
            crearContacto(numero,nombre,direccion)
        elif op == 2:
            nombre = str('')
            buscarContacto(nombre)
        elif op == 3:
            mostrarContactos()
        elif op == 4:
            nombre = input('Ingrese el nombre del contacto: ')
            modificarContacto(nombre)
        elif op == 5:
            nombre = input('Ingrese el nombre del contacto: ')
            eliminarContacto(nombre)
        elif op == 6:
            crearReporte()
        elif op == 7:
            print('Programa terminado.')
        else:
            print('Opción incorrecta.')
        input('Presione ENTER para continuar...')
main()