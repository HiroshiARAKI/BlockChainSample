from queue import Queue

from .Transaction import Transaction


class TransactionPool:
    def __init__(self):
        self.transactions = Queue()

    def put(self, transaction: Transaction):
        self.transactions.put(transaction)

    def get_transactions(self) -> list[Transaction]:
        return list(self.transactions.queue)

    def __repr__(self):
        return f'TransactionPool({self.get_transactions()})'
