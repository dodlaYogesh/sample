from django.db import models

# Create your models here.

class list(models.Model):
    name =models.CharField(max_length=250)
    age=models.IntegerField(default=1)
    address=models.CharField(max_length=250)



    def __str__(self):
        return self.name