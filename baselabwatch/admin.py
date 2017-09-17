from django.contrib import admin
from baselabwatch import models

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.School)
admin.site.register(models.Student)
admin.site.register(models.Subscription)
admin.site.register(models.UserReport)
