from dataclasses import dataclass

from .BlockHeader import BlockHeader
from .Transaction import Transaction


@dataclass
class Block:
    header: BlockHeader
    transactions: list[Transaction]
