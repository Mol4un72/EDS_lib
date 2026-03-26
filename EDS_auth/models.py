from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        UserEDSProfile.objects.create(user=instance)