while True:
    puntos = 0 
    Corect="Correcta "
    malo="Incorrecta "
    try:
        print("\n")
        entrada = input("Bienvenido a un examen , escribe (SI) para empezar: ")


    except KeyboardInterrupt:
        print("\n Adios")
        break

    if entrada.strip() == "SI":

            try:
                print("¿Cómo utilizarías el comando grep para buscar todas las líneas en un archivo de texto que contengan la palabra eror?")
                respuesta = input("Respuesta: ").strip().lower()
                if respuesta == "grep":
                    print(Corect)
                    puntos += 1
                else:
                    print(malo)
                print(" Explique cómo utilizar el comando awk para imprimir la segunda columna de un archivo CSV")
                respuesta = input("Respuesta: ").strip().lower()
                if respuesta == "awk":
                    print(Corect)
                    puntos += 1
                else:
                    print(malo)
                print(" ¿Cómo encontrar todos los archivos en un directorio y sus subdirectorios que tienen una extensión .txt?")
                respuesta = input("Respuesta: ").strip().lower()
                if respuesta == "find":
                    print(Corect)
                    puntos += 1
                else:
                    print(malo)
                print(" ¿Cómo usar el comando sed para reemplazar todas las instancias de la palabra old por new en un archivo de texto llamado example.txt?")
                respuesta = input("Respuesta: ").strip().lower()
                if respuesta == "sed":
                    print(Corect)
                    puntos += 1
                else:
                    print(malo)
                print("Explique cómo utilizar el comando rsync para copiar archivos de una carpeta local a un servidor remoto a través de SSH.")
                respuesta = input("Respuesta: ").strip().lower()
                if respuesta == "ysync":
                    print(Corect)
                    puntos += 1
                else:
                    print(malo)
            except KeyboardInterrupt:
                print("\n Adiós ")
                break
    print("\n\n")
    print("Resultado final ")
    print("Puntos obtenidos : (" + str(puntos) + "/5)")
    if puntos == 5: 
      print("Ganaste 10")
    elif puntos==4:
       print("Por poco 9")
    elif puntos==3:
       print("Ezfuerzate un poco mas 8 ")
    elif puntos<=2:
       print("Poco a poco 7")
    elif puntos<=1:
       print("Falta practicar")
      