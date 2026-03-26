from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .validators import validate_signature

class EDSBackend(BaseBackend):
    def authenticate(self, request, username=None, data=None, signature=None):
        if not all([username, data, signature]):
            return None

        try:
            # Знаходимо користувача за username
            user = User.objects.get(username=username)
            # Беремо його реальний ключ із профілю
            public_key = user.eds_profile.public_key
            
            # Викликаємо реальну криптографічну перевірку
            if validate_signature(data, signature, public_key):
                return user
                
        except (User.DoesNotExist, Exception):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None