from enum import Enum


class TransactionType(Enum):
    DEBIT = "debit"
    CREDIT = "credit"


class Transaction:
    _id: int
    _type: TransactionType
    _amount: int

    def __init__(self, id: int, type: TransactionType, amount: int):
        self._id = id
        self._type = type
        self._amount = amount

    # Atributos de solo lectura, para no modificar
    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def amount(self):
        return self._amount
