from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=2560)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title