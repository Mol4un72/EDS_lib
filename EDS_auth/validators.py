# django_ecp_auth/validators.py
from typing import Tuple
from .exceptions import InvalidSignatureError
import hashlib

def validate_signature(data: bytes, signature: bytes, cert: bytes) -> bool:
    """
    Перевірка ЕЦП: data - дані, signature - підпис, cert - сертифікат користувача
    """
    # Псевдо-логіка: реальний алгоритм залежить від формату ЕЦП
    digest = hashlib.sha256(data).digest()
    if digest != signature:
        raise InvalidSignatureError("Підпис не збігається з даними")
    return True