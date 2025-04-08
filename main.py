while True:
    # Solicitar información
    print(" \n Seleciona una de las siguientes opciones: \n 0. Exit")
    inputUser = int(input("Ingrese el número de su opción:"))

    # Terminar bucle
    if inputUser == 0:
        break
    else:
        print("La opción es inválida.")
