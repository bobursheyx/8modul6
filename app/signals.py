from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, **kwargs):
#     if created:
#         Token.objects.create(user=instance)



