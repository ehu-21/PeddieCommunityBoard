from django.db import models

# Create your models here.
class Post(models.Model):
    thread = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    desscription = models.CharField(max_length=200)
