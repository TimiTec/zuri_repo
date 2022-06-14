from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    Title= models.CharField(max_length=200)
    Text= models.TextField(max_length=200)
    Author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    Created_Date= models.DateTimeField()
    Published_date= models.DateTimeField()

