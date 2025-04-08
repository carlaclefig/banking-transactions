from ingest_data import ingest_data

while True:
    credit_transaction, debit_transaction = ingest_data()

    # Suma los montos de cada transación (crédito y débito)
    credit_sum = 0
    for transaction in credit_transaction:
        credit_sum += transaction.amount

    debit_sum = 0
    for transaction in debit_transaction:
        debit_sum += transaction.amount

    # Entrega el balance de todos los montos de las transaciones
    balance = round((credit_sum - debit_sum), 2)

    # Indica la mayor transación (crédito y débito)
    max_credit_transaction = credit_transaction[0]
    for transaction in credit_transaction:
        if transaction.amount > max_credit_transaction.amount:
            max_credit_transaction = transaction

    max_debit_transaction = debit_transaction[0]
    for transaction in debit_transaction:
        if transaction.amount > max_debit_transaction.amount:
            max_debit_transaction = transaction

    # Indica la mayor transación en total del archivo
    max_transaction = max_credit_transaction
    if max_debit_transaction.amount > max_transaction.amount:
        max_transaction = max_debit_transaction

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
        print(
            "\n\n Reporte de Transacciones"
            "\n --------------------------------------------------------"
            f"\n Balance Final: {balance}"
            f"\n Transacción de Mayor Monto: ID {max_transaction.id} - {max_transaction.amount}"
            f"\n Conteo de Transacciones: Crédito: {len(credit_transaction)} Débito: {len(debit_transaction)}"
            "\n --------------------------------------------------------\n"
        )
    else:
        print("La opción es inválida.")
