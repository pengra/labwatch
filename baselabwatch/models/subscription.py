from django.db import models
from baselabwatch.models import School, Student

class Subscription(models.Model):
    "A field for paid subscriptions."

    BILLING_CYCLES = (
        ('one', 'One Time'),
        ('month', 'Monthly'),
        ('year', 'Yearly')
    )

    expires = models.DateTimeField()
    school = models.OneToOneField(School, unique=True, related_name="subscription")
    billing_cycle = models.CharField(choices=BILLING_CYCLES, max_length=5)

    # plan_name = models.CharField(max_length=100)
    # Billing: https://apply.braintreegateway.com

    logger_access = models.BooleanField(blank=True, default=False)

    max_student_ids = models.IntegerField()
    max_kiosks = models.IntegerField()
    max_logs = models.IntegerField()
    student_rewards = models.BooleanField()
    data_intel = models.BooleanField()

    percentage_discount = models.FloatField()
    numeric_discount = models.IntegerField()

    @property
    def current_student_ids(self):
        "how many students are currently in use rn."
        return Student.objects.filter(school=self.school).count()
