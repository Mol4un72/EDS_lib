from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_user_keys():
    """Генерує пару: Приватний (віддати юзеру) та Публічний (записати в базу)"""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
    # Публічний ключ для бази даних
    public_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')

    # Приватний ключ, який юзер скачає як файл
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8')

    return private_pem, public_pem