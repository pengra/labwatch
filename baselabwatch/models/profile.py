"""
Extra data associated with the user.
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from baselabwatch.models.school import School


class Profile(models.Model):
    "Profile data for each user."
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, null=True, blank=True, related_name='teachers')

    engineer = models.BooleanField(default=False)
    librarian = models.BooleanField(default=False)
    techsavy = models.BooleanField(default=False)
    beta_tester = models.BooleanField(default=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    "Create a profile when a user is created"
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    "save the profile whenever the user is saved"
    instance.profile.save()
