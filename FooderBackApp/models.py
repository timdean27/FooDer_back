from django.db import models

# Create your models here.
class Gfood(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name