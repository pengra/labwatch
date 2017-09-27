from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
    "An object representing a single school."
    short_name = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255, unique=True, blank=True)
    primary_contact = models.OneToOneField(User, related_name='primary_contact_for', null=True)
    auth_code = models.CharField(max_length=32, unique=True)
    school_image = models.URLField()

    logger_access = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.short_name
