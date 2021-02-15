from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


@receiver(post_save, sender=User)
def auth_toke_create(sender, instance, created, *args, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        token.save()
