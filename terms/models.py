# legal/models.py
from django.db import models

class Policy(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

