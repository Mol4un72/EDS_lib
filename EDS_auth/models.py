from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserEDSProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eds_profile')
    public_key = models.TextField(verbose_name="Public key (PEM)", blank=True, null=True)

    def __str__(self):
        return f"EDS Profile: {self.user.username}"

# Цей код автоматично створює профіль при реєстрації юзера
@receiver(post_save, sender=User)
def create_user_eds_profile(sender, instance, created, **kwargs):
    if created:
        UserEDSProfile.objects.create(user=instance)