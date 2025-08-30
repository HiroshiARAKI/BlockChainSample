import json
from dataclasses import dataclass, asdict

from .HashUtil import hash_of


@dataclass
class BlockHeader:
    index: int
    timestamp: int
    nonce: int
    previous_hash: str
    merkle_root: str

    def get_hash(self) -> str:
        original = json.dumps(asdict(self), sort_keys=True).encode()
        return hash_of(original)

    def __repr__(self):
        return (f'BlockHeader('
                f'index={self.index}, '
                f'timestamp={self.timestamp}, '
                f'nonce={self.nonce}, '
                f'hash={self.get_hash()}, '
                f'previous_hash={self.previous_hash}, '
                f'merkle_root={self.merkle_root})')
