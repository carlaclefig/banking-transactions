import csv
from typing import List

from transaction import Transaction, TransactionType


def ingest_data():
    credit_transaction: List[Transaction] = []
    debit_transaction: List[Transaction] = []

    with open("data.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            id = int(row["id"])
            type = row["tipo"]
            amount = float(row["monto"])

            if type == "Crédito":
                transaction = Transaction(id, TransactionType.CREDIT, amount)
                credit_transaction.append(transaction)
            elif type == "Débito":
                transaction = Transaction(id, TransactionType.DEBIT, amount)
                debit_transaction.append(transaction)

    return credit_transaction, debit_transaction
