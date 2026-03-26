from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from .exceptions import InvalidSignatureError

def validate_signature(data: bytes, signature: bytes, public_key_pem: str) -> bool:
    """
    Реальна перевірка ЕЦП за стандартом RSA.
    """
    try:
        # 1. Завантажуємо публічний ключ із формату PEM (текст)
        public_key = serialization.load_pem_public_key(
            public_key_pem.encode()
        )

        # 2. Виконуємо перевірку підпису
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        # Якщо підпис невірний, library викине помилку
        raise InvalidSignatureError("Цифровий підпис недійсний!")