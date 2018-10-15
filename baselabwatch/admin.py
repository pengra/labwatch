from django.contrib import admin
from baselabwatch import models

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    search_fields = (
        'first_name',
        'last_name',
        'nick_name',
        'student_id',
    )
    

admin.site.register(models.Profile)
admin.site.register(models.School)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Subscription)
admin.site.register(models.UserReport)
