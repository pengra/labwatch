from django.db import models
from baselabwatch.models import School

class ImageCard(models.Model):
    "Model for card image."

    school = models.ForeignKey(School, blank=True, null=True)
    image = models.URLField(unique=True)
    source = models.URLField(blank=True)

    def __str__(self):
        return self.source if self.source else self.image