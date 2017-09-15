from django.db import models
from django import forms
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


class Kiosk(models.Model):
    "An object representing a kiosk available for a school to use."
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School)
    auth_code = models.CharField(max_length=32, unique=True)
    active = models.BooleanField(default=False)
    poll_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.school, self.name)


class Subscription(models.Model):
    "A field for paid subscriptions."

    BILLING_CYCLES = (
        ('one', 'One Time'),
        ('month', 'Monthly'),
        ('year', 'Yearly')
    )

    expires = models.DateTimeField()
    school = models.OneToOneField(School, unique=True, related_name="subscription")
    billing_cycle = models.CharField(choices=BILLING_CYCLES, max_length=5)

    # plan_name = models.CharField(max_length=100)
    # Billing: https://apply.braintreegateway.com

    max_student_ids = models.IntegerField()
    max_kiosks = models.IntegerField()
    max_logs = models.IntegerField()
    student_rewards = models.BooleanField()
    data_intel = models.BooleanField()
    
    percentage_discount = models.FloatField()
    numeric_discount = models.IntegerField()
