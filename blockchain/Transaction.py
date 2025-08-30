from dataclasses import dataclass


@dataclass
class Transaction:
    name: str

    def encode(self) -> bytes:
        return self.name.encode()
