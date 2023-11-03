from django.db import models
from datetime import datetime

# Create your models here.

class list(models.Model):
    name =models.CharField(max_length=250)
    age=models.IntegerField()
    address=models.CharField(max_length=250)
    time=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name