import csv
from typing import List

from transaction import Transaction, TransactionType


def ingest_data(file_name: str) -> List[Transaction]:
    transactions: List[Transaction] = []

    with open(file_name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            id = int(row["id"])
            type = row["tipo"]
            amount = float(row["monto"])

            if type == "Crédito":
                transaction = Transaction(id, TransactionType.CREDIT, amount)
                transactions.append(transaction)
            elif type == "Débito":
                transaction = Transaction(id, TransactionType.DEBIT, amount)
                transactions.append(transaction)

    return transactions
