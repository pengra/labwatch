import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
    "An object representing a single school."
    short_name = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255, unique=True, blank=True)
    primary_contact = models.OneToOneField(User, related_name='primary_contact_for', null=True)
    auth_code = models.UUIDField(max_length=32, unique=True, default=uuid.uuid4)
    school_image = models.URLField(default="https://imgur.com/5Zx4W1p.png")

    def __str__(self):
        return self.short_name
