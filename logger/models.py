from django.db import models

# Create your models here.


class Student(models.Model):
    "An object representing a student."

    YEAR_IN_SCHOOL_CHOICES = (
        ('9', 'Freshman'),
        ('10', 'Sophomore'),
        ('11', 'Junior'),
        ('12', 'Senior'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_id = models.IntegerField(unique=True)
    teacher = models.CharField(max_length=255, blank=True)
    grade = models.CharField(
        max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, blank=True)

    # Potential future uses
    email = models.EmailField(blank=True)

    # Used for logging
    signed_in = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Log(models.Model):
    "A timestamp on top of a card scan/name input."

    SIGN_MODE = (
        ('IN', 'Sign in'),
        ('OUT', 'Sign out'),
    )

    INPUT_MODE = (
        ('CARD', 'Card Scan'),
        ('NAME', 'Name input'),
    )
    
    student = models.ForeignKey(Student)
    mode = models.CharField(max_length=3, choices=SIGN_MODE)
    input_mode = models.CharField(max_length=4, choices=INPUT_MODE, default=INPUT_MODE[0][0])
    timestamp = models.DateTimeField(auto_now_add=True)

