import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class lo(models.Model):
    name = models.TextField(null=True)
    namet = models.TextField(null=True)
    stat = models.CharField(default=1,max_length=2)
    tiam = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name