from django.db import models
import datetime
from products.models import list

# Create your models here.

class Olist(models.Model):
    view=models.OneToOneField(list,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.view.name