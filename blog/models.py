from django.db import models
from django.utils import timezone


class Post(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateField(default=timezone.now())
    text = models.TextField(max_length=10000, blank=True)
