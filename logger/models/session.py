from django.db import models
from django.utils import timezone
from baselabwatch.models import Student
# Create your models here.

class StudentSession(models.Model):
    "A log of a student login/logout."

    # Models actually depend on these indexes now
    # Do not change.

    INPUT_MODE = (
        ('CARD', 'Card Scan'),  # 0
        ('NAME', 'Name input'),  # 1
        ('EMAL', 'Email'),  # 2
        ('NICK', 'Nickname input'),  # 3
        ('ADMI', 'Admin input')  # 4
    )

    student = models.ForeignKey(Student)

    sign_in_mode = models.CharField(max_length=4, choices=INPUT_MODE)
    sign_out_mode = models.CharField(max_length=4, choices=INPUT_MODE, blank=True)

    sign_in_timestamp = models.DateTimeField(default=timezone.now)
    sign_out_timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.student)
