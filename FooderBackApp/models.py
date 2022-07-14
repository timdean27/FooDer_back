from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Gfood(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_url = models.TextField()
    Liked_Foods = ArrayField(models.IntegerField(), blank=True)
    disLiked_Foods = ArrayField(models.IntegerField(), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name