from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + self.user
    
    def get_absolute_url(self):
        return reverse('home', args=(str(self.id)))