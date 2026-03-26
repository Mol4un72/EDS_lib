from django.db import models
from django.contrib.auth.models import User

class UserEDSProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eds_profile')
    # Публічний ключ зберігаємо як текст (формат PEM)
    public_key = models.TextField(verbose_name="Public key (PEM)", help_text="Вставте сюди вміст файлу .pub")

    def __str__(self):
        return f"Profile EDS: {self.user.username}"