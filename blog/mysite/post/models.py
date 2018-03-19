from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_created=True, auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return "%s" %self.title

