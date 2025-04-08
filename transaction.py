from enum import Enum


class TransactionType(Enum):
    DEBIT = "debit"
    CREDIT = "credit"


class Transaction:
    # Atributos privados (inmodificables fuera de la clase)
    __id: int
    __type: TransactionType
    __amount: float

    def __init__(self, id: int, type: TransactionType, amount: float):
        self.__id = id
        self.__type = type
        self.__amount = amount

    # Atributos de solo lectura
    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        return self.__type

    @property
    def amount(self):
        return self.__amount
