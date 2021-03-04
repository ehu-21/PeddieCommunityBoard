from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    """
    Written by Rohan Nunugonda. Creates the Post model on which the Post form is created
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + self.user
    
    def get_absolute_url(self):
        """
        Written by Rohan Nunugonda. Supposed to redirect the post to the PostDetail Form after being created, but for some reason
        does not work.
        """
        return reverse('forum:postDetail', args=(str(self.id)))