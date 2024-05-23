import random

nommbre_archivo="pruebasEjercicio.csv"
separador = ("----" * 40) + "\n"
#listaCodigoAleatorio = [random.randint(0,100000)]

try:
    with open(nommbre_archivo):
        print(separador)
        print("El archivo si existe")

        listaCodigoAleatorio = [random.randint(0,100000)]
        print(separador)
        print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
        print(separador)
        opcion = input("¿Que operacion deseas realizar?: \n")

        if opcion == "1":
            print("Nuevo registro\n")
            archivo=open("pruebasEjercicio.csv","a")
            nombre= input("Ingrese el nombre: ")

            print("Numero de departamentos validos:\n1)-Ventas. 2)-Compras. 3)-Contabilidad. 4)-Producciones. 5)-Sistemas.\n")
            departamento= int(input("Ingrese un coidgo de un departamento: "))
            print(f"Se ha capturado el empleado {nombre},con un codigo {listaCodigoAleatorio} que esta en el departamento {departamento}.")
            archivo.write("°°°Nombre   Codigo   Departamento°°°\n")
            archivo.write(nombre + ",  " + (str(listaCodigoAleatorio)) + ",  " + (str(departamento)) + ".\n")
            archivo.close()
            while opcion >="0":
                listaCodigoAleatorio = [random.randint(0,100000)]
                print(separador)
                print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
                print(separador)
                opcion = input("¿Que operacion deseas realizar?: \n")
                if opcion == "1":
                    print("Nuevo registro\n")
                    archivo=open("pruebasEjercicio.csv","a")
                    nombre= input("Ingrese el nombre: ")

                    print("Numero de departamentos validos:\n1)-Ventas. 2)-Compras. 3)-Contabilidad. 4)-Producciones. 5)-Sistemas.\n")
                    departamento= int(input("Ingrese un coidgo de un departamento: "))
                    print(f"Se ha capturado el empleado {nombre},con un codigo {listaCodigoAleatorio} que esta en el departamento {departamento}.")
                    archivo.write("°°°Nombre   Codigo   Departamento°°°\n")
                    archivo.write(nombre + ",  " + (str(listaCodigoAleatorio)) + ",  " + (str(departamento)) + ".\n")
                    archivo.close()

                elif opcion == "2":
                    print("Mostrar registros\n")
                    archivo=open("pruebasEjercicio.csv")
                    print(archivo.read())
                    archivo.close()

                elif opcion == "3":
                    archivo=open("pruebasEjercicio.csv","a")
                    archivo.truncate(0)
                    print("Registros eliminados!!\n ")
                    archivo.close()
                else:
                    print("Debes de elegir una opción valida >:v\n ")

        elif opcion == "2":
            print("Mostrar registros\n")
            archivo=open("pruebasEjercicio.csv")
            print(archivo.read())
            archivo.close()
            while opcion >="0":
                listaCodigoAleatorio = [random.randint(0,100000)]
                print(separador)
                print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
                print(separador)
                opcion = input("¿Que operacion deseas realizar?: \n")
                if opcion == "1":
                    print("Nuevo registro\n")
                    archivo=open("pruebasEjercicio.csv","a")
                    nombre= input("Ingrese el nombre: ")

                    print("Numero de departamentos validos:\n1)-Ventas. 2)-Compras. 3)-Contabilidad. 4)-Producciones. 5)-Sistemas.\n")
                    departamento= int(input("Ingrese un coidgo de un departamento: "))
                    print(f"Se ha capturado el empleado {nombre},con un codigo {listaCodigoAleatorio} que esta en el departamento {departamento}.")
                    archivo.write("°°°Nombre   Codigo   Departamento°°°\n")
                    archivo.write(nombre + ",  " + (str(listaCodigoAleatorio)) + ",  " + (str(departamento)) + ".\n")
                    archivo.close()

                elif opcion == "2":
                    print("Mostrar registros\n")
                    archivo=open("pruebasEjercicio.csv")
                    print(archivo.read())
                    archivo.close()

                elif opcion == "3":
                    archivo=open("pruebasEjercicio.csv","a")
                    archivo.truncate(0)
                    print("Registros eliminados!!\n ")
                    archivo.close()
                else:
                    print("Debes de elegir una opción valida >:v\n ")

        elif opcion == "3":
            archivo=open("pruebasEjercicio.csv","a")
            archivo.truncate(0)
            print("Registros eliminados!!\n ")
            archivo.close()
            while opcion >="0":
                listaCodigoAleatorio = [random.randint(0,100000)]
                print(separador)
                print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
                print(separador)
                opcion = input("¿Que operacion deseas realizar?: \n")
                if opcion == "1":
                    print("Nuevo registro\n")
                    archivo=open("pruebasEjercicio.csv","a")
                    nombre= input("Ingrese el nombre: ")

                    print("Numero de departamentos validos:\n1)-Ventas. 2)-Compras. 3)-Contabilidad. 4)-Producciones. 5)-Sistemas.\n")
                    departamento= int(input("Ingrese un coidgo de un departamento: "))
                    print(f"Se ha capturado el empleado {nombre},con un codigo {listaCodigoAleatorio} que esta en el departamento {departamento}.")
                    archivo.write("°°°Nombre   Codigo   Departamento°°°\n")
                    archivo.write(nombre + ",  " + (str(listaCodigoAleatorio)) + ",  " + (str(departamento)) + ".\n")
                    archivo.close()

                elif opcion == "2":
                    print("Mostrar registros\n")
                    archivo=open("pruebasEjercicio.csv")
                    print(archivo.read())
                    archivo.close()

                elif opcion == "3":
                    archivo=open("pruebasEjercicio.csv","a")
                    archivo.truncate(0)
                    print("Registros eliminados!!\n ")
                    archivo.close()
                else:
                    print("Debes de elegir una opción valida >:v\n ")

        else:
            print("Debes de elegir una opción valida >:v\n ")
            while opcion >="0":
                listaCodigoAleatorio = [random.randint(0,100000)]
                print(separador)
                print("MENU de opciones: \n\n1)- Dar de alta un empleado.\n2)- Mostrar datos.\n3)- Eliminar registros.\nDejar en blanco para salir.")
                print(separador)
                opcion = input("¿Que operacion deseas realizar?: \n")
                if opcion == "1":
                    print("Nuevo registro\n")
                    archivo=open("pruebasEjercicio.csv","a")
                    nombre= input("Ingrese el nombre: ")

                    print("Numero de departamentos validos:\n1)-Ventas. 2)-Compras. 3)-Contabilidad. 4)-Producciones. 5)-Sistemas.\n")
                    departamento= int(input("Ingrese un coidgo de un departamento: "))
                    print(f"Se ha capturado el empleado {nombre},con un codigo {listaCodigoAleatorio} que esta en el departamento {departamento}.")
                    archivo.write("°°°Nombre   Codigo   Departamento°°°\n")
                    archivo.write(nombre + ",  " + (str(listaCodigoAleatorio)) + ",  " + (str(departamento)) + ".\n")
                    archivo.close()

                elif opcion == "2":
                    print("Mostrar registros\n")
                    archivo=open("pruebasEjercicio.csv")
                    print(archivo.read())
                    archivo.close()

                elif opcion == "3":
                    archivo=open("pruebasEjercicio.csv","a")
                    archivo.truncate(0)
                    print("Registros eliminados!!\n ")
                    archivo.close()
                else:
                    print("Debes de elegir una opción valida >:v\n ")
except FileNotFoundError:
    print("El archivo no existe, no se puede cargar los datos. ")
