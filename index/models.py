from django.db import models

class UserReport(models.Model):
    "Model for bug reports/questions."

    REPORT_TYPES = (
        ('bug', 'Question'),
        ('question', 'Question'),
    )

    report_type = models.CharField(max_length=255, choices=REPORT_TYPES)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    dealt_with = models.BooleanField(default=False)

    def __str__(self):
        return self.title
