import csv
import unicodedata
from typing import List

from transaction import Transaction, TransactionType


def ingest_data(file_name: str) -> List[Transaction]:
    transactions: List[Transaction] = []

    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            id = int(row["id"])
            type = normalize_string(row["tipo"])
            amount = float(row["monto"])

            if type == "credito":
                transaction = Transaction(id, TransactionType.CREDIT, amount)
                transactions.append(transaction)
            elif type == "debito":
                transaction = Transaction(id, TransactionType.DEBIT, amount)
                transactions.append(transaction)

        if len(transactions) == 0:
            print("\n 📌 El archivo no cuenta con transacciones.")

        return transactions


def normalize_string(tex):
    # Eliminar acentos y convertir a minúsculas
    normalize_text = (
        unicodedata.normalize("NFKD", tex).encode("ascii", "ignore").decode("ascii")
    )
    # Elimina espacios y convierte a minúsculas
    return normalize_text.strip().lower()
