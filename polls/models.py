from django.db import models
from registration.models import Kiosk

# Create your models here.

class PollQuestion(models.Model):
    "A question model for asking students questions."
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    kiosk = models.ManyToManyField(Kiosk)

    def __str__(self):
        return self.question_text

class PollChoice(models.Model):
    "A choice for a question."
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text