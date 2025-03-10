from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
