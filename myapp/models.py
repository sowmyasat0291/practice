from django.db import models

# Create your models here.
class mytable(models.Model):
    name = models.CharField(max_length=20)
    year = models.DateField()
    