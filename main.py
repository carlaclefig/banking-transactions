from ingest_data import ingest_data
from transaction_operations import generate_report, print_report

transactions = []
while len(transactions) == 0:
    user_input = input('Ingresar el nombre del archivo o "SALIR": ')

    if user_input.upper() == "SALIR":
        print("\n Hasta pronto. 👋")
        exit()

    transactions = ingest_data(user_input)

while True:
    # Opciones
    print(
        "\n Seleciona una de las siguientes opciones:"
        "\n 1. Reporte de Transacciones "
        "\n 0. Salir "
    )
    try:
        user_input = input("Ingrese el número de su opción: ")
        option_user = int(user_input)
    except ValueError:
        print("\n 🚨 Ingrese un número. 🚨")
        continue

    # Verificar que no coloque una opción invalida
    if option_user < 0 or option_user > 1:
        print("\n ❌ Opción no válida. ❌")
        continue

    # Termina el bucle
    if option_user == 0:
        print("\n Hasta pronto. 👋")
        break

    if option_user == 1:
        # Llama a la función que calcula la opción 1
        balance, max_transaction, credit_count, debit_count = generate_report(
            transactions
        )
        print_report(balance, max_transaction, credit_count, debit_count)
