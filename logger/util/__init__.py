from baselabwatch.models import Student
from logger.models import StudentSession

def get_last_log(student):
    "Get last StudentSession for Student."
    return StudentSession.objects.filter(student=student).last()

