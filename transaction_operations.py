from typing import List

from transaction import Transaction, TransactionType


def generate_report(transaction_list: List[Transaction]):
    if len(transaction_list) == 0:
        return

    credit_sum = 0
    debit_sum = 0
    balance = 0
    max_transaction = transaction_list[0]
    credit_count = 0
    debit_count = 0

    for transaction in transaction_list:
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

    return balance, max_transaction, credit_count, debit_count


def print_report(
    balance: float, max_transaction: Transaction, credit_count: int, debit_count: int
):
    # Inicia la creación del mensaje
    msg = f"""\n 
                 Reporte de Transacciones
                --------------------------------------------------------
                 Balance Final: {balance}
                 Transacción de Mayor Monto: ID {max_transaction.id} - {max_transaction.amount}
                 Conteo de Transacciones: Crédito: {credit_count} Débito: {debit_count}\n """

    print(msg)
