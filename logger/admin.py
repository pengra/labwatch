from django.contrib import admin
from logger import models


# Register your models here.
admin.site.register(models.StudentSession)
admin.site.register(models.Kiosk)
admin.site.register(models.PollQuestion)
admin.site.register(models.PollChoice)
admin.site.register(models.ImageCard)
