from django.db import models


class Post(models.Model):
    text = models.TextField()
    thumb = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.text[:50]


# Create your models here.
