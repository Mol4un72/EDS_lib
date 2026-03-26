# django_ecp_auth/backend.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .validators import validate_signature
from .exceptions import InvalidSignatureError, UserNotFoundError
from typing import Optional

class ECPBackend(BaseBackend):
    """
    Авторизація через ЕЦП
    """
    def authenticate(self, request, data: bytes = None, signature: bytes = None) -> Optional[User]:
        from django.conf import settings

        cert_path = settings.ECP_CERT_DIR
        # Тут треба завантажити сертифікат користувача (псевдо)
        cert = b"сертифікат"

        try:
            if validate_signature(data, signature, cert):
                # шукаємо користувача за username або серією сертифіката
                try:
                    user = User.objects.get(username="example_user")
                    return user
                except User.DoesNotExist:
                    raise UserNotFoundError("Користувача не знайдено")
        except InvalidSignatureError as e:
            return None

    def get_user(self, user_id: int) -> Optional[User]:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None