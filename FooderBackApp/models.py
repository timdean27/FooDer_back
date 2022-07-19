from django.db import models

# Create your models here.
class Gfood(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user_string = models.CharField(max_length=100, default='unknown_user')

    def __str__(self):
        return self.name