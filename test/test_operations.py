import unittest

from transaction import Transaction, TransactionType
from transaction_operations import generate_report

transactions = [
    Transaction(1, TransactionType.CREDIT, 100.0),
    Transaction(2, TransactionType.DEBIT, 50.0),
    Transaction(id=3, type=TransactionType.CREDIT, amount=200.0),
    Transaction(4, TransactionType.DEBIT, 30.0),
]


class TestGenerateReport(unittest.TestCase):
    def test_balance(self):
        balance, _, _, _ = generate_report(transactions)
        self.assertEqual(balance, 220.0)

    def test_max_transaction(self):
        _, max_transaction, _, _ = generate_report(transactions)
        self.assertEqual(max_transaction.id, 3)
        self.assertEqual(max_transaction.amount, 200)

    def test_credit_count(self):
        _, _, credit_count, _ = generate_report(transactions)
        self.assertEqual(credit_count, 2)

    def test_debit_count(self):
        _, _, _, debit_count = generate_report(transactions)
        self.assertEqual(debit_count, 2)
