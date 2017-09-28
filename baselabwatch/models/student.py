from django.db import models
from baselabwatch.models.school import School

# Create your models here.


class Student(models.Model):
    "An object representing a student."

    YEAR_IN_SCHOOL_CHOICES = (
        ('09', 'Freshman'),
        ('10', 'Sophomore'),
        ('11', 'Junior'),
        ('12', 'Senior'),
        ('GD', 'Graduated')
    )

    first_name = models.CharField(
        max_length=255, help_text="Student First Name")
    last_name = models.CharField(max_length=255, help_text="Student Last Name")
    nick_name = models.CharField(max_length=255, blank=True,
                help_text="Should the student forget his ID, he can type his name or his/her 'nickname'.")
    student_id = models.IntegerField(
        unique=True, help_text="Student ID number")
    teacher = models.CharField(
        max_length=255, blank=True, help_text="Student teacher")
    grade = models.CharField(
        max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, blank=True)

    # School association
    school = models.ForeignKey(
        School, help_text="School this student attends.", null=True)

    # Potential future uses
    email = models.EmailField(
        blank=True, help_text="Student can submit email if they choose to")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
