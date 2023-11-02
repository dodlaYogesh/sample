from django.db import models
import datetime

# Create your models here.

class list(models.Model):
    name =models.CharField(max_length=250)
    age=models.IntegerField(default=1)
    address=models.CharField(max_length=250)
    time=models.DateTimeField

    def __str__(self):
        return self.name