from django.db import models

# Create your models here.
class sanjar(models.Model):
    name = models.TextField(max_length=255)
    username = models.TextField(max_length=255)