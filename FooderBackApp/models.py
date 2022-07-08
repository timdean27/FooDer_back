from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Gfood(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    Liked_Foods = ArrayField(models.IntegerField(), blank=True)
    disLiked_Foods = ArrayField(models.IntegerField(), blank=True)

    def __str__(self):
        return self.name