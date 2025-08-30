import hashlib


def hash_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
