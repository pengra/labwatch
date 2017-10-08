import uuid

from django.db import models

from baselabwatch.models import School
from logger.models import PollQuestion


class Kiosk(models.Model):
    "An object representing a kiosk available for a school to use."
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School)
    auth_code = models.UUIDField(max_length=32, unique=True, default=uuid.uuid4)
    poll = models.ForeignKey(PollQuestion, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.school, self.name)
