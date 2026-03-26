# django_ecp_auth/exceptions.py
class ECPAuthError(Exception):
    """Базова помилка пакету"""

class InvalidSignatureError(ECPAuthError):
    """Підпис недійсний"""

class UserNotFoundError(ECPAuthError):
    """Користувача не знайдено"""