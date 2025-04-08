from typing import Optional

from ingest_data import ingest_data
from transaction import Transaction, TransactionType

file_name = input("Ingresar el nombre del archivo: ")
transactions = ingest_data(file_name)

while True:
    credit_sum = 0
    debit_sum = 0
    balance = 0
    max_transaction: Optional[Transaction] = None
    credit_count = 0
    debit_count = 0

    if len(transactions) != 0:
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

    # Solicitar información
    print(
        "\n Seleciona una de las siguientes opciones:"
        "\n 0. Exit "
        "\n 1.Reporte de Transacciones \n"
    )
    inputUser = int(input("Ingrese el número de su opción: "))

    # Terminar bucle
    if inputUser == 0:
        break
    elif inputUser == 1:
        # Verifica que exista por lo menos 1 transacción
        if len(transactions) != 0 and max_transaction is not None:
            print(
                "\n\n Reporte de Transacciones"
                "\n --------------------------------------------------------"
                f"\n Balance Final: {balance}"
                f"\n Transacción de Mayor Monto: ID {max_transaction.id} - {max_transaction.amount}"
                f"\n Conteo de Transacciones: Crédito: {credit_count} Débito: {debit_count}"
                "\n --------------------------------------------------------\n"
            )
        else:
            print("Aún no hay transacciones!")

    else:
        print("La opción es inválida.")
