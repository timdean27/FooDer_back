from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Gfood(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user_string = models.CharField(max_length=100, default='unknown_user')
    owner = models.ForeignKey(User, related_name='Gfood' , on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name




            