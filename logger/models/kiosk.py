from django.db import models
from logger.models import PollQuestion
from baselabwatch.models import School

class Kiosk(models.Model):
    "An object representing a kiosk available for a school to use."
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School)
    auth_code = models.CharField(max_length=32, unique=True)
    poll = models.ForeignKey(PollQuestion, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.school, self.name)

