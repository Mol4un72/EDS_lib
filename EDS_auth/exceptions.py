class EDSError(Exception):
    """Базова помилка для всіх проблем з ЕЦП"""
    def __init__(self, message="Помилка електронного підпису"):
        self.message = message
        super().__init__(self.message)

class InvalidSignatureError(EDSError):
    """Підпис не пройшов математичну перевірку (validator)"""
    def __init__(self, message="Цифровий підпис недійсний"):
        super().__init__(message)

class UserNotFoundError(EDSError):
    """Користувача не знайдено в базі"""
    def __init__(self, message="Користувача з таким іменем не існує"):
        super().__init__(message)

class MissingPublicKeyError(EDSError):
    """У юзера немає збереженого публічного ключа"""
    def __init__(self, message="Публічний ключ не знайдено у профілі користувача"):
        super().__init__(message)