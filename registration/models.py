from django.db import models
from django import forms

# Create your models here.

class School(models.Model):
    "An object representing a single school."
    name = models.CharField(max_length=255, unique=True)
    primary_contact = models.OneToOneField('Teacher', related_name='primary_contact_for', null=True)
    auth_code = models.CharField(max_length=32, unique=True)
    school_image = models.URLField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    "An account that allows a librarian/Teacher to view their school data."
    school = models.ForeignKey(School)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)