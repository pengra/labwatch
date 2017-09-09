from django.db import models

# Create your models here.

class School(models.Model):
    "An object representing a single school."
    name = models.CharField(max_length=255, unique=True)
    contact_email = models.EmailField()
    auth_code = models.CharField(max_length=32, unique=True)
    school_image = models.URLField()
