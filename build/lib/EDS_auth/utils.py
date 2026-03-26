# django_ecp_auth/utils.py
from typing import List

def load_certificates(path: str) -> List[bytes]:
    """
    Завантажує всі сертифікати з директорії
    """
    # Псевдо-реалізація
    return [b"cert1", b"cert2"]