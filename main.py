from blockchain import BlockChain
from blockchain.Transaction import Transaction

if __name__ == '__main__':
    blockchain = BlockChain(difficulty=2)

    blockchain.add_transaction(Transaction(name="Alice"))
    blockchain.print_chain()

    blockchain.mine_block()
    blockchain.print_chain()

    blockchain.add_transaction(Transaction(name="Bob"))
    blockchain.add_transaction(Transaction(name="John"))
    blockchain.mine_block()
    blockchain.print_chain()
