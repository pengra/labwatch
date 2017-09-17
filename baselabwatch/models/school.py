from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
    "An object representing a single school."
    name = models.CharField(max_length=255, unique=True)
    primary_contact = models.OneToOneField(User, related_name='primary_contact_for', null=True)
    teachers = models.ManyToManyField(User, blank=True, related_name='associated_school')
    auth_code = models.CharField(max_length=32, unique=True)
    school_image = models.URLField()

    def __str__(self):
        return self.name
