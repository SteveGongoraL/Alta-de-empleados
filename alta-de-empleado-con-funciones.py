import time
nommbre_archivo="altasEmpleados.csv"
separador = ("----" * 40) + "\n"
listaCodigo = []
def primera_Opcion():
    print("Nuevo registro\n")
    archivo=open("altasEmpleados.csv","a")
    nombre= input("Ingrese el nombre y apellido del empleado: ")
    print("Numero de departamentos validos:\n1)-Ventas.\t2)-Compras.\t3)-Contabilidad.\t4)-Producciones.\t5)-Sistemas.\n")
    departamento= int(input("Ingrese un codigo de un departamento: "))
    while departamento>5:
        departamento= int(input("Dime un numero de departamento valido: "))
        if departamento>5:
            departamento= int(input("Dime un numero de departamento valido: "))
    else:
        print("Numero de departamento valido!!!")
    codigoPedido= int(input("Dime un codigo para tu empleado: "))
    while codigoPedido in listaCodigo:
        codigoPedido= int(input("Codigo invalido, dime otro: "))
        if codigoPedido in listaCodigo:
            codigoPedido= int(input("Codigo invalido, dime otro: "))
    else:
        print("Codigo valido")
        listaCodigo.append(codigoPedido)
        print(f"Se ha capturado el empleado {nombre.title()},con un codigo {codigoPedido} que esta en el departamento {departamento}.")
        archivo.write("°°Nombre"+",    "+"Codigo"+",    "+"Departamento°°"+"\n")
        archivo.write(nombre.title() + ",   " + (str(codigoPedido)) + ",   " + (str(departamento)) + "\n")
        archivo.close()
    time.sleep(2)
def segunda_Opcion():
    print("Mostrar registros".center(80,"*"))
    archivo=open("altasEmpleados.csv")
    print(archivo.read())
    archivo.close()
    time.sleep(4)
def tercera_Opcion():
    archivo=open("altasEmpleados.csv","a")
    archivo.truncate(0)
    print("Registros eliminados!!".center(80,"*"))
    archivo.close()
    time.sleep(2)
try:
    with open(nommbre_archivo):
        print(separador)
        print("El archivo si existe.\n")
        print(separador)
        print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
        print(separador)
        opcion = input("¿Que operacion deseas realizar?: \n")
        if opcion == "1":
            primera_Opcion()
            while opcion >="0":
                print(separador)
                print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
                print(separador)
                opcion = input("¿Que operacion deseas realizar?: \n")
                if opcion == "1":
                    primera_Opcion()
                elif opcion == "2":
                    segunda_Opcion()
                elif opcion == "3":
                    tercera_Opcion()
                else:
                    print("Debes de elegir una opción valida >:v\n ")
        elif opcion == "2":
            segunda_Opcion()
            while opcion >="0":
                print(separador)
                print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
                print(separador)
                opcion = input("¿Que operacion deseas realizar?: \n")
                if opcion == "1":
                    primera_Opcion()
                elif opcion == "2":
                    segunda_Opcion()
                elif opcion == "3":
                    tercera_Opcion()
                else:
                    print("Debes de elegir una opción valida >:v\n ")
        elif opcion == "3":
            tercera_Opcion()
            while opcion >="0":
                print(separador)
                print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
                print(separador)
                opcion = input("¿Que operacion deseas realizar?: \n")
                if opcion == "1":
                    primera_Opcion()
                elif opcion == "2":
                    segunda_Opcion()
                elif opcion == "3":
                    tercera_Opcion()
                else:
                    print("Debes de elegir una opción valida >:v\n ")
        else:
            print("Debes de elegir una opción valida >:v\n ")
            while opcion >="0":
                print(separador)
                print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
                print(separador)
                opcion = input("¿Que operacion deseas realizar?: \n")
                if opcion == "1":
                    primera_Opcion()
                elif opcion == "2":
                    segunda_Opcion()
                elif opcion == "3":
                    tercera_Opcion()
                else:
                    print("Debes de elegir una opción valida >:v\n ")
except FileNotFoundError:
    f=open("altasEmpleados.csv","w")
    print("\n\n*****El archivo no existe, no se puede cargar los datos.*****\n***Pero se creo un archivo con nombre 'altasEmpleados' vuelva a intentar correr el programa.***\n")
    f.close()