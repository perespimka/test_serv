from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    owner = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(upload_to='pics/', null=True, blank=True)
    def __str__(self):
        return self.title
        
class Commentary(models.Model):
    post = models.ForeignKey(BlogPost, models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    owner = models.ForeignKey(User, models.CASCADE)