import time

from .Block import Block
from .BlockHeader import BlockHeader
from .HashUtil import hash_of
from .Transaction import Transaction
from .TransactionPool import TransactionPool


class BlockChain:
    transaction_pool = TransactionPool()
    chain: list[Block] = []

    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.chain.append(self._create_genesis_block())
        print(f'BlockChain is created (difficulty={self.difficulty}).')

    def add_transaction(self, transaction: Transaction):
        print(f'Add transaction ({transaction})')
        self.transaction_pool.put(transaction)

    def mine_block(self) -> Block:
        print('Start mining block.')
        print(f'- Current transaction pool: {self.transaction_pool}')
        print(f'- Current chain: {self.chain}')
        prev: Block = self.chain[-1]

        index = prev.header.index + 1
        ts = time.time_ns()
        nonce = 0
        prev_hash = prev.header.get_hash()
        transactions = self.transaction_pool.get_transactions()

        while True:
            merkle_root = self._calc_merkle_root(transactions)
            new_block: Block = Block(
                header=BlockHeader(
                    index=index,
                    timestamp=ts,
                    nonce=nonce,
                    previous_hash=prev_hash,
                    merkle_root=merkle_root,
                ),
                transactions=transactions,
            )
            new_hash = new_block.header.get_hash()
            if new_hash[:self.difficulty] == '0' * self.difficulty:
                self.chain.append(new_block)
                self.transaction_pool = TransactionPool()
                print(f'-- Successfully mined new block with nonce={nonce}.')
                return new_block

            nonce += 1

    def _calc_merkle_root(self, transactions: list[Transaction]) -> str:
        return self._calk_merkle_root_by_hashes([t.name for t in transactions])

    def _calk_merkle_root_by_hashes(self, hash_srcs: list[str]) -> str:
        if len(hash_srcs) == 0:
            return hash_of(b'')
        elif len(hash_srcs) == 1:
            return hash_of(hash_srcs[0].encode())
        elif len(hash_srcs) % 2 == 1:
            hash_srcs.append(hash_srcs[-1])

        next_hashes: list[str] = []

        for i in range(0, len(hash_srcs), 2):
            next_hash_src = hash_srcs[i] + hash_srcs[i + 1]
            next_hashes.append(hash_of(next_hash_src.encode()))

        return self._calk_merkle_root_by_hashes(next_hashes)

    def print_chain(self):
        print(f'Current BlockChain:\n- chain={self.chain} \n- transaction_pool={self.transaction_pool}')

    @staticmethod
    def _create_genesis_block() -> Block:
        return Block(
            header=BlockHeader(
                index = 0,
                timestamp = time.time_ns(),
                nonce = 0,
                previous_hash = '',
                merkle_root = '',
            ),
            transactions=[],
        )
