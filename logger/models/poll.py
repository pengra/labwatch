from django.db import models

class PollQuestion(models.Model):
    "A question model for asking students questions."
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class PollChoice(models.Model):
    "A choice for a question."
    # allowed to be null so the teacher can delete a poll choice but still have it show up
    # under student sign in logs.
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE, null=True, blank=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
