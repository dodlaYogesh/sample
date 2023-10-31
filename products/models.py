from django.db import models
import datetime

# Create your models here.

class list(models.Model):
    title =models.CharField(max_length=250)
    tag=models.CharField(max_length=250)
