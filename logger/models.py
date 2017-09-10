from django.db import models
from polls.models import PollChoice
from registration.models import School

# Create your models here.


class Student(models.Model):
    "An object representing a student."

    YEAR_IN_SCHOOL_CHOICES = (
        ('9', 'Freshman'),
        ('10', 'Sophomore'),
        ('11', 'Junior'),
        ('12', 'Senior'),
    )

    first_name = models.CharField(max_length=255, help_text="Student First Name")
    last_name = models.CharField(max_length=255, help_text="Student Last Name")
    nick_name = models.CharField(max_length=255, blank=True, help_text="Should the student forget his ID, he can type his name or his/her 'nickname'.")
    student_id = models.IntegerField(unique=True, help_text="Student ID number")
    teacher = models.CharField(max_length=255, blank=True, help_text="Student teacher")
    grade = models.CharField(
        max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, blank=True)

    # School association
    school = models.ForeignKey(School, help_text="School this student attends.", null=True)

    # Potential future uses
    email = models.EmailField(blank=True, help_text="Student can submit email if they choose to")

    # Used for logging
    signed_in = models.BooleanField(default=False, help_text="Status regarding student is signed in or not")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Log(models.Model):
    "A timestamp on top of a card scan/name input."

    SIGN_MODE = (
        ('IN', 'Sign in'),
        ('OUT', 'Sign out'),
    )

    INPUT_MODE = (
        ('CARD', 'Card Scan'), #0
        ('NAME', 'Name input'), #1
        ('EMAL', 'Email'), #2
        ('NICK', 'Nickname input'), #3
        ('ADMI', 'Admin input') #4
    )

    student = models.ForeignKey(Student)
    mode = models.CharField(max_length=3, choices=SIGN_MODE)
    input_mode = models.CharField(
        max_length=4, choices=INPUT_MODE, default=INPUT_MODE[0][0])
    timestamp = models.DateTimeField(auto_now_add=True)

    # poll add on
    poll_answer = models.ForeignKey(PollChoice, blank=True, null=True)

    def __str__(self):
        return "{}: {}".format(self.student, self.mode)
