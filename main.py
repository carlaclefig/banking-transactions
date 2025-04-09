from typing import Optional

from ingest_data import ingest_data
from transaction import Transaction, TransactionType

file_name = input("Ingresar el nombre del archivo: ")
transactions = ingest_data(file_name)

while True:
    # Opciones
    print(
        "\n Seleciona una de las siguientes opciones:"
        "\n 1. Reporte de Transacciones "
        "\n 0. Salir "
    )
    try:
        input_user = input("Ingrese el número de su opción: ")
        option_user = int(input_user)
    except ValueError:
        print("\n 🚨 Ingrese un número válido. 🚨")
        continue

    # Verificar que no coloque una opción invalida
    if option_user < 0 or option_user > 1:
        print("⚠️ Opción no válida. ⚠️")
        continue

    # Termina el bucle
    if option_user == 0:
        break

    if option_user == 1:
        if len(transactions) == 0:
            print("¡Aún no hay transacciones!")
            continue  # Vuelve a las opciones

        # Cálculo solo con opción 1
        credit_sum = 0
        debit_sum = 0
        balance = 0
        max_transaction: Optional[Transaction] = None
        credit_count = 0
        debit_count = 0

        max_transaction = transactions[0]
        for transaction in transactions:
            # Suma los montos de cada transación (crédito y débito)
            if transaction.type == TransactionType.CREDIT:
                credit_sum += transaction.amount
                credit_count += 1

            elif transaction.type == TransactionType.DEBIT:
                debit_sum += transaction.amount
                debit_count += 1

            # Indica la mayor transación (crédito y débito)
            if max_transaction.amount < transaction.amount:
                max_transaction = transaction

        # Entrega el balance de todos los montos de las transaciones
        balance = round((credit_sum - debit_sum), 2)

        # Inicia la creación del mensaje
        msg = f"""\n\n Reporte de Transacciones
            \n --------------------------------------------------------
            \n Balance Final: {balance}"""

        if max_transaction is not None:
            msg += f"\n Transacción de Mayor Monto: ID {max_transaction.id} - {max_transaction.amount}"

        msg += (
            f"\n Conteo de Transacciones: Crédito: {credit_count} Débito: {debit_count}"
        )

        print(msg)
