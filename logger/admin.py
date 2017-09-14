from django.contrib import admin
from logger import models

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    pass

class LogAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Log, LogAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.KioskSession)
