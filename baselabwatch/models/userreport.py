from django.db import models
from django.contrib.auth.models import User

class UserReport(models.Model):
    "Model for bug reports/questions."

    REPORT_TYPES = (
        ('bug', 'Bug'),
        ('question', 'Question'),
    )

    report_type = models.CharField(max_length=10, choices=REPORT_TYPES)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    dealt_with = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.title