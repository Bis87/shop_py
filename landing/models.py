from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subscribers(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)