from django.db import models
from django.contrib.auth.models import User
from registration.models import School


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
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.title


class ImageCard(models.Model):
    "Model for card image."

    school = models.ForeignKey(School, blank=True, null=True)
    image = models.URLField(unique=True)


'''
    class SpreadsheetUpload(models.Model):
        """
        Spreadsheet for bulk student uploads.
        Cannot be utilized until an S3 bucket is paid for.
        Details here: 
        - https://stackoverflow.com/questions/39425217/django-heroku-uploading-files
        - https://devcenter.heroku.com/articles/s3-upload-python
        feelsbadman.jpg
        """
        FILE_FORMATS = (
            ('xls', 'Excel'),
            ('xml', 'XML')
        )
        mode = models.CharField(
            max_length=10, choices=FILE_FORMATS, default=FILE_FORMATS[1][0])

        spreadsheet = models.FileField()

        studentid = models.CharField(max_length=255)
        fname = models.CharField(max_length=255)
        lname = models.CharField(max_length=255)
        grade = models.CharField(max_length=255, blank=True)
        teacher = models.CharField(max_length=255, blank=True)
        nickname = models.CharField(max_length=255, blank=True)
        email = models.CharField(max_length=255, blank=True)
        row = models.CharField(max_length=255, blank=True)
        data_starts_on = models.IntegerField(blank=True, null=True)
        parent = models.CharField(max_length=255, blank=True)
'''
