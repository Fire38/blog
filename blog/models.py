from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)


class Blog(models.Model):
    name = models.CharField(max_length=40, blank=False)
    owner = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=300, blank=False)
    text = models.TextField(max_length=5000, blank=False)
    blog = models.ForeignKey(Blog, default='1', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title[:60]